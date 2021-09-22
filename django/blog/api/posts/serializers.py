from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
    slug = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
