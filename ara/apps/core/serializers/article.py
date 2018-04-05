from rest_framework import serializers

from apps.core.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    from apps.core.serializers.topic import TopicSerializer
    from apps.core.serializers.board import BoardSerializer

    parent_topic = TopicSerializer()
    parent_board = BoardSerializer()

    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        from apps.session.models import UserProfile
        if not obj.is_anonymous:
            userProfile = UserProfile.objects.filter(user = obj.created_by)
            if userProfile.first() is None:
                return None
            return userProfile.first().user_nickname
        else:
            return "익명" 


class ArticleDetailActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    from apps.core.serializers.topic import TopicSerializer
    from apps.core.serializers.board import BoardSerializer
    from apps.core.serializers.article_log import ArticleUpdateLogSerializer

    my_vote = serializers.SerializerMethodField()
    my_report = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    article_current_page = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()

    parent_topic = TopicSerializer()
    parent_board = BoardSerializer()
    article_update_logs = ArticleUpdateLogSerializer(
        many=True,
        source='article_update_log_set',
    )

    def get_created_by(self, obj):
        from apps.session.models import UserProfile
        if not obj.is_anonymous:
            userProfile = UserProfile.objects.filter(user = obj.created_by)
            if userProfile.first() is None:
                return None
            return userProfile.first().user_nickname
        else:
            return "익명"


    def get_my_vote(self, obj):
        from apps.core.models import Vote

        try:
            return obj.vote_set.get(
                created_by=self.context['request'].user,
            ).is_positive

        except Vote.DoesNotExist:
            return None

    def get_my_report(self, obj):
        from apps.core.models import Report
        from apps.core.serializers.report import ReportSerializer

        try:
            return ReportSerializer(
                instance=obj.report_set.get(
                    reported_by=self.context['request'].user,
                ),
            ).data

        except Report.DoesNotExist:
            return None

    def get_comments(self, obj):
        from apps.core.serializers.comment import CommentSerializer

        return CommentSerializer(
            obj.comment_set.all(), many=True,
            **{'context': {'request': self.context.get('request')}}
        ).data

    def get_article_current_page(self, obj):
        view = self.context.get('view')

        paginator = view.paginator.django_paginator_class(view.filter_queryset(view.get_queryset()), view.paginator.page_size)

        for page_number in paginator.page_range:
            page = paginator.page(page_number)

            if obj.id in [object.id for object in page.object_list]:
                return page_number

class ArticleCreateActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'is_anonymous',
            'is_content_sexual',
            'is_content_social',
            'use_signature',
            'parent_topic',
            'parent_board',
            'attachments',
        )


class ArticleUpdateActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title',
            'content',
            'is_content_sexual',
            'is_content_social',
            'attachments',
        )
