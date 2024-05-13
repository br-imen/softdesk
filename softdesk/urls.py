"""
URL configuration for softdesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView
from comments.views import CommentDetail, CommentList
from user.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from project.views import ProjectListCreateAPIView,ProjectRetrieveUpdateDestroyAPIView
from issues.views import IssueListCreateAPIView, IssueRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('api/projects/<int:project_pk>/issues/', IssueListCreateAPIView.as_view(), name='issue-list-create'),
    path('api/projects/<int:project_pk>/issues/<int:pk>/', IssueRetrieveUpdateDestroyAPIView.as_view(), name='issue-detail'),
    path('api/issues/<int:issue_pk>/comments/', CommentList.as_view(), name='comment-list'),
    path('api/issues/<int:issue_pk>/comments/<uuid:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
