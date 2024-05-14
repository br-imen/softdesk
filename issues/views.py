from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import (ContributorPermission,
                        AuthorOrAssigneesPermission,)
from softdesk.permissions import AuthorPermission
from project.models import Project
from .models import Issue
from .serializers import IssueSerializer


class IssueListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, ContributorPermission]

    def perform_create(self, serializer):
        """
        Perform a create on the serializer, ensuring project is included.
        """
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        serializer.save(author=self.request.user, project=project)

class IssueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated, ContributorPermission]
        elif self.request.method in ['PUT', 'DELETE']:
            permission_classes = [IsAuthenticated, AuthorPermission]
        elif self.request.method == 'PATCH':
            if len(self.request.data) == 1 and 'status' in self.request.data:
                permission_classes = [IsAuthenticated, AuthorOrAssigneesPermission]
            else:
                permission_classes = [IsAuthenticated, AuthorPermission]
        return [permission() for permission in permission_classes]

    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        context = super().get_serializer_context()
        context['project_pk'] = self.kwargs['project_pk']
        return context
