from .permissions import IsAuthorOrReadOnly, IsContributorOrAuthor
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .models import Issue
from .serializers import IssueSerializer

class IssueListCreateAPIView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]


class IssueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]