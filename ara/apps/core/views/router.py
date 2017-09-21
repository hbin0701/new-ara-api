from rest_framework import routers

from apps.core.views.viewsets import *


router = routers.SimpleRouter()


# ArticleViewSet

router.register(
    prefix=r'articles',
    viewset=ArticleViewSet,
)

# CommentViewSet

router.register(
    prefix=r'comments',
    viewset=CommentViewSet,
)


