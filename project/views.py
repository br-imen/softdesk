from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from softdesk.permissions import (
    AuthorPermission,
    AuthorOrContributorPermission,
)


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that
        this view requires.
        """
        if self.request.method == "GET":
            permission_classes = [
                IsAuthenticated,
                AuthorOrContributorPermission,
            ]
        elif self.request.method in ["PUT", "PATCH", "DELETE"]:
            permission_classes = [IsAuthenticated, AuthorPermission]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
