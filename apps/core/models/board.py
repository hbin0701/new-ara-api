from django.db import models

from django_extensions.db.fields import AutoSlugField

from ara.db.models import MetaDataModel


class Board(MetaDataModel):
    class Meta(MetaDataModel.Meta):
        verbose_name = '게시판'
        verbose_name_plural = '게시판 목록'

    slug = AutoSlugField(
        populate_from=[
            'en_name',
        ],
    )
    ko_name = models.CharField(
        unique=True,
        max_length=32,
        verbose_name='게시판 국문 이름',
    )
    en_name = models.CharField(
        unique=True,
        max_length=32,
        verbose_name='게시판 영문 이름',
    )
    ko_description = models.TextField(
        verbose_name='게시판 국문 소개',
    )
    en_description = models.TextField(
        verbose_name='게시판 영문 소개',
    )

    def __str__(self):
        return self.ko_name
