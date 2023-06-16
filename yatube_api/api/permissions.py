from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Запрашивать список всех публикаций или отдельную публикацию
    может любой пользователь.
    Создавать новую публикацию может только
    аутентифицированный пользователь.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
