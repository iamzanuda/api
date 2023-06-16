from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet,
                    UserViewSet)

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'users', UserViewSet, basename='users')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='post_comments')
router.register(r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
                CommentViewSet, basename='post_comments_id')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
