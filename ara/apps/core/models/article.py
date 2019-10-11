import bs4
import bleach
import json

from django.db import models, IntegrityError
from django.conf import settings
from rest_framework import status, response

from ara.db.models import MetaDataModel


class Article(MetaDataModel):
    class Meta(MetaDataModel.Meta):
        verbose_name = '문서'
        verbose_name_plural = '문서 목록'

    title = models.CharField(
        max_length=256,
        verbose_name='제목',
    )
    content = models.TextField(
        verbose_name='본문',
    )
    content_text = models.TextField(
        editable=False,
        verbose_name='text 형식 본문',
    )

    is_anonymous = models.BooleanField(
        default=False,
        verbose_name='익명',
    )
    is_content_sexual = models.BooleanField(
        default=False,
        verbose_name='성인/음란성 내용',
    )
    is_content_social = models.BooleanField(
        default=False,
        verbose_name='정치/사회성 내용',
    )

    hit_count = models.IntegerField(
        default=0,
        verbose_name='조회수',
    )
    positive_vote_count = models.IntegerField(
        default=0,
        verbose_name='좋아요 수',
    )
    negative_vote_count = models.IntegerField(
        default=0,
        verbose_name='싫어요 수',
    )

    created_by = models.ForeignKey(
        on_delete=models.CASCADE,
        to=settings.AUTH_USER_MODEL,
        db_index=True,
        related_name='article_set',
        verbose_name='작성자',
    )
    parent_topic = models.ForeignKey(
        on_delete=models.CASCADE,
        to='core.Topic',
        null=True,
        blank=True,
        default=None,
        db_index=True,
        related_name='article_set',
        verbose_name='말머리',
    )
    parent_board = models.ForeignKey(
        on_delete=models.CASCADE,
        to='core.Board',
        db_index=True,
        related_name='article_set',
        verbose_name='게시판',
    )

    attachments = models.ManyToManyField(
        to='core.Attachment',
        blank=True,
        db_index=True,
        verbose_name='첨부 파일(들)',
    )

    commented_at = models.DateTimeField(
        null=True,
        default=None,
        verbose_name='마지막 댓글 시간',
    )

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            if self.parent_topic:
                assert self.parent_topic.parent_board == self.parent_board

        except AssertionError:
            raise IntegrityError('self.parent_board should be parent_board of self.parent_topic')

        try:
            self.sanitize(self.title, json.loads(self.content))  # True
        except json.decoder.JSONDecodeError as e:
            print(f'JSONDecodeError: {e}\n{self.content}')
            return response.response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except AssertionError as e:
            print(f'AssertionError: {e}')
            return response.response(status=status.HTTP_400_BAD_REQUEST)

        self.content_text = ' '.join(bs4.BeautifulSoup(self.content, features='html5lib').find_all(text=True))

        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    # TODO: hit_count property should be cached
    def update_hit_count(self):
        self.hit_count = self.article_read_log_set.count()

        self.save()

    # TODO: positive_vote_count, negative_vote_count properties should be cached
    def update_vote_status(self):
        self.positive_vote_count = self.vote_set.filter(is_positive=True).count()
        self.negative_vote_count = self.vote_set.filter(is_positive=False).count()

        self.save()

    @property
    def comments_count(self):
        from apps.core.models import Comment

        return Comment.objects.filter(parent_article=self).count()

    @property
    def nested_comments_count(self):
        from apps.core.models import Comment

        return Comment.objects.filter(
            models.Q(parent_article=self) |
            models.Q(parent_comment__parent_article=self)
        ).count()

    @staticmethod
    def sanitize(title, content):
        assert title == bleach.clean(title), f'title contains invalid text;\n{title}'
        assert type(content) == dict, f'article content is not JSONForamt;\n{content}'
        assert content.get("type") == "doc", f'article content must begin with doc;\n{content}'
        assert list(content.keys()) == ["type", "content"], f'invalid or missing keys in article content;\n{content}'
        assert type(content.get("content")) == list, f'content is not list;\n{content}'

        following = {
            "doc": ["paragraph", "heading"],
            "paragraph": ["text"],
            "heading": ["text"],
            "text": [],
            "marks": ["bold", "code"]
        }

        necessary = {
            "paragraph": ["type", "content"],
            "heading": ["type", "attrs", "content"],
            "text": ["type", "text"]
        }

        available = {
            "paragraph": ["type", "content"],
            "heading": ["type", "attrs", "content"],
            "text": ["type", "text", "marks"]
        }

        def sanitize_rec(content, prev):
            assert content.get("type") in following[prev], f'invalid type {content.get("type")} under {prev};\n{content}'
            assert type(content.get("content", [])) == list, f'content is not list;\n{content}'
            assert type(content.get("marks", [])) == list, f'marks is not list;\n{content}'
            assert type(content.get("attrs", {"level": 0}).get("level")) == int, f'invalid level in attr;\n{content}'
            assert type(content.get("text", "")) == str, f'text is not string;\n{content}'
            assert all(key in content.keys() for key in necessary[content.get("type")]), f'missing key for type {content.get("type")}; this type needs {necessary[content.get("type")]};\n{content}'
            assert all(key in available[content.get("type")] for key in content.keys()), f'invalid key for type {content.get("type")}; available key for this type is {available[content.get("type")]};\n{content}'
            content_chk = all(sanitize_rec(cont, content.get("type")) for cont in content.get("content", []))
            marks_chk = all(mark.get("type") in following["marks"] for mark in content.get("marks", []))
            return content_chk and marks_chk

        return all(sanitize_rec(cont, "doc") for cont in content.get("content"))
