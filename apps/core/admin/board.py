from django.contrib import admin

from reversion_compare.admin import CompareVersionAdmin

from apps.core.models import Board


@admin.register(Board)
class BoardAdmin(CompareVersionAdmin):
    list_display = (
        'ko_name',
        'en_name',
    )
    search_fields = (
        'ko_name',
        'en_name',
        'ko_description',
        'en_description',
    )
