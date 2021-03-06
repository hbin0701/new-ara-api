from rest_framework import mixins

from ara.classes.viewset import ActionAPIViewSet

from apps.core.models import (
    ArticleReadLog,
    Block,
    Report,
)
from apps.core.permissions.report import ReportPermission
from apps.core.serializers.report import (
    ReportSerializer,
    ReportCreateActionSerializer,
)


class ReportViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    ActionAPIViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    action_serializer_class = {
        'create': ReportCreateActionSerializer,
    }
    permission_classes = (
        ReportPermission,
    )

    def get_queryset(self):
        queryset = super(ReportViewSet, self).get_queryset()

        queryset = queryset.filter(
            reported_by=self.request.user,
        ).select_related(
            'reported_by',
            'reported_by__profile',
            'parent_article',
            'parent_article__created_by',
            'parent_article__created_by__profile',
            'parent_article__parent_topic',
            'parent_article__parent_board',
            'parent_comment',
            'parent_comment__created_by',
            'parent_comment__created_by__profile',
        ).prefetch_related(
            'parent_article__comment_set',
            'parent_article__comment_set__comment_set',
            'parent_article__attachments',
            'parent_article__article_update_log_set',
            Block.prefetch_my_block(self.request.user, prefix='parent_article__'),
            Block.prefetch_my_block(self.request.user, prefix='parent_comment__'),
            ArticleReadLog.prefetch_my_article_read_log(self.request.user, prefix='parent_article__'),
        )

        return queryset

    def perform_create(self, serializer):
        serializer.save(
            reported_by=self.request.user,
        )
