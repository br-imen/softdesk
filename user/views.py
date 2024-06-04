from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import UserPermission


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions
        that this view requires.
        """
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated, IsAdminUser]
        elif self.request.method in ["POST"]:
            permission_classes = []
        return [permission() for permission in permission_classes]



class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions
        that this view requires.
        """
        if self.request.method == "GET":
            permission_classes = [IsAuthenticated, UserPermission]
        elif self.request.method in ["PUT", "PATCH", "DELETE"]:
            permission_classes = [IsAuthenticated, UserPermission]
        return [permission() for permission in permission_classes]

