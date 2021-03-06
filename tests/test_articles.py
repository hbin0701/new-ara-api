import pytest
from django.test import TestCase
from django.utils import timezone

from apps.core.models import Article, Topic, Board
from tests.conftest import RequestSetting


@pytest.fixture(scope='class')
def set_board(request):
    request.cls.board = Board.objects.create(
        slug="test board",
        ko_name="테스트 게시판",
        en_name="Test Board",
        ko_description="테스트 게시판입니다",
        en_description="This is a board for testing"
    )


@pytest.fixture(scope='class')
def set_topic(request):
    """set_board 먼저 적용"""
    request.cls.topic = Topic.objects.create(
        slug="test topic",
        ko_name="테스트 토픽",
        en_name="Test Topic",
        ko_description="테스트용 토픽입니다",
        en_description="This is topic for testing",
        parent_board=request.cls.board
    )


@pytest.fixture(scope='class')
def set_article(request):
    """set_board 먼저 적용"""
    request.cls.article = Article.objects.create(
            title="example article",
            content="example content",
            content_text="example content text",
            is_anonymous=False,
            is_content_sexual=False,
            is_content_social=False,
            hit_count=0,
            positive_vote_count=0,
            negative_vote_count=0,
            created_by=request.cls.user,
            parent_topic=request.cls.topic,
            parent_board=request.cls.board,
            commented_at=timezone.now()
    )


@pytest.mark.usefixtures('set_user_client', 'set_user_client2', 'set_board', 'set_topic', 'set_article')
class TestArticle(TestCase, RequestSetting):
    def test_list(self):
        # article 개수를 확인하는 테스트
        res = self.http_request(self.user, 'get', 'articles')
        assert res.data.get('num_items') == 1

        Article.objects.create(
            title="example article",
            content="example content",
            content_text="example content text",
            is_anonymous=False,
            is_content_sexual=False,
            is_content_social=False,
            hit_count=0,
            positive_vote_count=0,
            negative_vote_count=0,
            created_by=self.user,
            parent_topic=self.topic,
            parent_board=self.board,
            commented_at=timezone.now()
        )

        Article.objects.create(
            title="example article",
            content="example content",
            content_text="example content text",
            is_anonymous=False,
            is_content_sexual=False,
            is_content_social=False,
            hit_count=0,
            positive_vote_count=0,
            negative_vote_count=0,
            created_by=self.user,
            parent_topic=self.topic,
            parent_board=self.board,
            commented_at=timezone.now()
        )

        res = self.http_request(self.user, 'get', 'articles')
        assert res.data.get('num_items') == 3

    def test_get(self):
        # article 조회가 잘 되는지 확인
        res = self.http_request(self.user, 'get', f'articles/{self.article.id}').data
        assert res.get('title') == self.article.title
        assert res.get('content') == self.article.content
        assert res.get('content_text') == self.article.content_text
        assert res.get('is_anonymous') == self.article.is_anonymous
        assert res.get('is_content_sexual') == self.article.is_content_sexual
        assert res.get('is_content_social') == self.article.is_content_social
        assert res.get('positive_vote_count') == self.article.positive_vote_count
        assert res.get('negative_vote_count') == self.article.negative_vote_count
        assert res.get('created_by')['username'] == self.user.username
        assert res.get('parent_topic')['ko_name'] == self.article.parent_topic.ko_name
        assert res.get('parent_board')['ko_name'] == self.article.parent_board.ko_name

    def test_anonymous_writer(self):
        # 익명의 글쓴이가 익명임을 확인
        article = Article.objects.create(
            title="example article",
            content="example content",
            content_text="example content text",
            is_anonymous=True,
            is_content_sexual=False,
            is_content_social=False,
            hit_count=0,
            positive_vote_count=0,
            negative_vote_count=0,
            created_by=self.user,
            parent_topic=self.topic,
            parent_board=self.board,
            commented_at=timezone.now()
        )

        assert self.http_request(self.user, 'get', f'articles/{article.id}').data.get('created_by') == '익명'

    def test_create(self):
        # test_create: HTTP request (POST)를 이용해서 생성
        # user data in dict
        user_data = {
            "title": "article for test_create",
            "content": "content for test_create",
            "content_text": "content_text for test_create",
            "is_anonymous": True,
            "is_content_sexual": False,
            "is_content_social": False,
            "parent_topic": self.topic.id,
            "parent_board": self.board.id
        }
        # convert user data to JSON
        self.http_request(self.user, 'post', 'articles', user_data)
        assert Article.objects.filter(title='article for test_create')

    def test_update_hit_counts(self):
        previous_hit_count = self.article.hit_count
        res = self.http_request(self.user2, 'get', f'articles/{self.article.id}').data
        assert res.get('hit_count') == previous_hit_count + 1
        assert Article.objects.get(id=self.article.id).hit_count == previous_hit_count + 1

    def test_delete_by_non_writer(self):
        # 글쓴이가 아닌 사람은 글을 지울 수 없음
        assert Article.objects.filter(id=self.article.id)
        self.http_request(self.user2, 'delete', f'articles/{self.article.id}')
        assert Article.objects.filter(id=self.article.id)

    def test_delete_by_writer(self):
        # 글쓴이는 본인 글을 지울 수 있음
        assert Article.objects.filter(id=self.article.id)
        self.http_request(self.user, 'delete', f'articles/{self.article.id}')
        assert not Article.objects.filter(id=self.article.id)

    def test_update_votes(self):
        # user가 만든 set_article의 positive vote, negative vote 를 set_user_client2를 이용해서 바꿈 (투표 취소 가능한지, 둘다 중복투표 불가능한지 확인)
        # positive vote 확인
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_positive')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 1
        assert article.negative_vote_count == 0

        # 같은 사람이 positive_vote 여러 번 투표할 수 없음
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_positive')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 1
        assert article.negative_vote_count == 0

        # positive_vote 취소
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_cancel')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 0

        # positive_vote 취소 후 재투표
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_positive')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 1
        assert article.negative_vote_count == 0
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_cancel')

        # negative vote 확인
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_negative')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 1

        # 같은 사람이 negative vote 여러 번 투표할 수 없음
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_negative')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 1

        # negative vote 투표 취소
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_cancel')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 0

        # negative vote 취소 후 재투표
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_negative')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 1

        # 중복 투표 시도 (negative 투표한 상태로 positive 투표하면, positive 1개로 바뀌어야함)
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_positive')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 1
        assert article.negative_vote_count == 0

        # 중복 투표 시도 (positive 투표한 상태로 negative 투표하면, negative 1개로 바뀌어야함)
        self.http_request(self.user2, 'post', f'articles/{self.article.id}/vote_negative')
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 1

    def test_self_vote(self):
        # 자신이 쓴 게시물은 좋아요 / 싫어요를 할 수 없음
        resp = self.http_request(self.user, 'post', f'articles/{self.article.id}/vote_positive')
        assert resp.status_code == 403
        assert resp.data["message"] is not None
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 0

        resp = self.http_request(self.user, 'post', f'articles/{self.article.id}/vote_negative')
        assert resp.status_code == 403
        assert resp.data["message"] is not None
        article = Article.objects.get(id=self.article.id)
        assert article.positive_vote_count == 0
        assert article.negative_vote_count == 0
