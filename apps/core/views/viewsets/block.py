from rest_framework import mixins

from ara.classes.viewset import ActionAPIViewSet

from apps.core.models import Block
from apps.core.serializers.block import (
    BlockSerializer,
    BlockCreateActionSerializer,
)


class BlockViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   ActionAPIViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    action_serializer_class = {
        'create': BlockCreateActionSerializer,
    }

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)

        queryset = queryset.select_related(
            'user',
            'user__profile',
        )

        return queryset

    def perform_create(self, serializer):
        serializer.save(
            blocked_by=self.request.user,
        )
