from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from issues.models import Issue
from .serializers import CommentSerializer
from .permissions import ContributorPermission
from softdesk.permissions import AuthorPermission


class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def perform_create(self, serializer):
        issue_id = self.kwargs.get("issue_pk")
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(author=self.request.user, issue=issue)

    def get_queryset(self):
        issue_pk = self.kwargs["issue_pk"]
        project_pk = self.kwargs["project_pk"]
        return Comment.objects.filter(
            issue__project__id=project_pk, issue__pk=issue_pk
        )


class CommentRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = CommentSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions
        that this view requires.
        """
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated, ContributorPermission]
        elif self.request.method in ["PUT", "PATCH", "DELETE"]:
            permission_classes = [IsAuthenticated, AuthorPermission]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        project_pk = self.kwargs["project_pk"]
        issue_pk = self.kwargs["issue_pk"]
        uuid = self.kwargs["pk"]
        return Comment.objects.filter(
            issue__project__id=project_pk, issue_id=issue_pk, id=uuid
        )
