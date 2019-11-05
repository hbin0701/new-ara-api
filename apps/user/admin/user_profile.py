from django.contrib import admin

from reversion_compare.admin import CompareVersionAdmin

from apps.user.models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(CompareVersionAdmin):
    list_filter = (
        'see_sexual',
        'see_social',
    )
    list_display = (
        'uid',
        'sid',
        'nickname',
        'user',
    )
    search_fields = (
        'uid',
        'sid',
        'nickname',
        'user',
    )
