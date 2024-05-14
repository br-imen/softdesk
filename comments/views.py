from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from issues.models import Issue
from .serializers import CommentSerializer
from .permissions import ContributorPermission
from softdesk.permissions import AuthorPermission


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]


    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_pk')
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(author=self.request.user, issue=issue)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated, ContributorPermission]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsAuthenticated, AuthorPermission]            
        return [permission() for permission in permission_classes]


