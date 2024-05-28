from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    issue_id = serializers.ReadOnlyField(source="issue.id")

    class Meta:
        model = Comment
        fields = ["id", "description", "author", "issue_id", "created_time"]
        read_only_fields = ["id", "author", "created_time", "issue_id"]
