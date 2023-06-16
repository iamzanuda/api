from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Group, Post, User
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Вьюсет Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,
                          permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Сохраняем текущего пользователя."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет Comment."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,
                          permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        """Сохраняем полученный обьект и автора."""
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        """Сохраняем коментарий к конкретному посту."""
        post = get_object_or_404(Post, id=self.kwargs.get("post_id"))
        return post.comments.all()


class FollowViewSet(viewsets.ModelViewSet):
    """Вьюсет Follow."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'following')
    search_fields = ('following__username',)

    def get_queryset(self):
        """Получаем подписчиков."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """Сохраняем текущего пользователя."""
        serializer.save(user=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    """Вьюсет User."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
