from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post, User


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор моддели Group."""
    class Meta:
        fields = '__all__'
        model = Group


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор моддели Post."""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор моддели Comment."""
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор моддели Follow."""
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate_following(self, data):
        """Запрещаем подписку на себя."""
        if data == self.context.get('request').user:
            raise serializers.ValidationError(
                "Нельзя подписываться на себя.")
        return data


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор моддели User."""
    class Meta:
        fields = '__all__'
        model = User
