from rest_framework import viewsets

from ara.classes.viewset import ActionAPIViewSet

from apps.core.models import Article, ArticleReadLog, \
        ArticleUpdateLog
from apps.core.filters.article import ArticleFilter
from apps.core.permissions.article import ArticlePermission
from apps.core.serializers.article import ArticleSerializer, \
    ArticleCreateActionSerializer, ArticleUpdateActionSerializer

from datetime import datetime


class ArticleViewSet(viewsets.ModelViewSet, ActionAPIViewSet):
    queryset = Article.objects.all()
    filter_class = ArticleFilter
    serializer_class = ArticleSerializer
    action_serializer_class = {
        'create': ArticleCreateActionSerializer,
        'update': ArticleUpdateActionSerializer,
        'partial_update': ArticleUpdateActionSerializer,
    }
    permission_classes = (
        ArticlePermission,
    )

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user,
        )

    def perform_update(self, serializer):
        instance = serializer.instance

        ArticleUpdateLog.objects.create(
            updated_by=instance.created_by,
            article=instance,
            content=instance.content,
            is_content_sexual=instance.is_content_sexual,
            is_content_social=instance.is_content_social,
            use_signature=instance.use_signature,
            parent_topic=instance.parent_topic,
            parent_board=instance.parent_board,
        )

        return super(ArticleViewSet, self).perform_update(serializer)

    def retrieve(self, request, *args, **kwargs):
        article_read_log, created = ArticleReadLog.objects.get_or_create(
            read_by=self.request.user,
            article=self.get_object(),
        )

        if not created:
            article_read_log.created_at = datetime.now()
            article_read_log.save()

        return super(ArticleViewSet, self).retrieve(request, *args, **kwargs)