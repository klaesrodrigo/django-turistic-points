from rest_framework.serializers import ModelSerializer
from comments.models import Comment


class CommentSearializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "user", "comment")
