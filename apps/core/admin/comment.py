from django.contrib import admin

from reversion_compare.admin import CompareVersionAdmin

from apps.core.models import (
    BestComment,
    CommentDeleteLog,
)


@admin.register(CommentDeleteLog)
class CommentDeleteLogAdmin(CompareVersionAdmin):
    list_filter = (
        'comment',
    )
    list_display = (
        'deleted_by',
        'comment',
        'created_at',
    )
    search_fields = (
        'deleted_by__username',
    )


@admin.register(BestComment)
class BestCommentAdmin(CompareVersionAdmin):
    pass
