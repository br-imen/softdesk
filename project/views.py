from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsAuthorOrReadOnly, IsContributorOrAuthor



class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Ensure that the current user is the author of the project
        if serializer.instance.author != self.request.user:
            raise PermissionDenied("You are not allowed to update this project.")
        serializer.save()
        return Response(status=status.HTTP_200_OK)


    def perform_destroy(self, instance):
        # Ensure that the current user is the author of the project
        if instance.author != self.request.user:
            raise PermissionDenied("You are not allowed to delete this project.")
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer