from rest_framework import generics
from .models import Comment
from issues.models import Issue
from .serializers import CommentSerializer
from .permissions import IsContributorOrReadOnly

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_pk')
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(author=self.request.user, issue=issue)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


