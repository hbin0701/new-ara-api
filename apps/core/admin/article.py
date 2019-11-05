from django.contrib import admin

from reversion_compare.admin import CompareVersionAdmin

from apps.core.models import (
    Article,
    BestArticle,
    ArticleReadLog,
    ArticleDeleteLog,
)


@admin.register(Article)
class ArticleAdmin(CompareVersionAdmin):
    list_filter = (
        'is_anonymous',
        'is_content_sexual',
        'is_content_social',
        'parent_topic',
        'parent_board',
    )
    list_display = (
        'title',
        'hit_count',
        'positive_vote_count',
        'negative_vote_count',
        'is_anonymous',
        'is_content_sexual',
        'is_content_social',
        'created_by',
        'parent_topic',
        'parent_board',
    )
    search_fields = (
        'title',
        'content',
        'ko_description',
        'en_description',
    )


@admin.register(ArticleReadLog)
class ArticleReadLogAdmin(CompareVersionAdmin):
    list_filter = (
        'article',
    )
    list_display = (
        'read_by',
        'article',
        'created_at',
    )
    search_fields = (
        'read_by__username',
    )


@admin.register(ArticleDeleteLog)
class ArticleDeleteLogAdmin(CompareVersionAdmin):
    list_filter = (
        'article',
    )
    list_display = (
        'deleted_by',
        'article',
        'created_at',
    )
    search_fields = (
        'deleted_by__username',
    )


@admin.register(BestArticle)
class BestArticleAdmin(CompareVersionAdmin):
    pass
