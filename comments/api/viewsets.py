from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializers import CommentSearializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSearializer
