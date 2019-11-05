from django.contrib import admin
from django.contrib.auth.admin import (
    UserAdmin as BaseUserAdmin,
    GroupAdmin as BaseGroupAdmin,
)
from django.contrib.auth.models import (
    User,
    Group,
    Permission,
)

from reversion_compare.admin import CompareVersionAdmin


admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(CompareVersionAdmin, BaseUserAdmin):
    def reversion_register(self, model, **options):
        options['follow'] = (
            'groups',
            'user_permissions',
        )

        super().reversion_register(model, **options)


@admin.register(Group)
class GroupAdmin(CompareVersionAdmin, BaseGroupAdmin):
    def reversion_register(self, model, **options):
        options['follow'] = (
            'permissions',
        )

        super().reversion_register(model, **options)


@admin.register(Permission)
class PermissionAdmin(CompareVersionAdmin):
    pass
