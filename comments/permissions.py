from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Comment
from issues.models import Issue


class ContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create
    """
    def has_permission(self, request, view):
        # For actions that relate to a specific existing object
        if 'pk' in view.kwargs:
            obj = get_object_or_404(Comment, pk=view.kwargs['pk'])
            return request.user in obj.issue.project.contributors.all()

        if 'issue_pk' in view.kwargs:
            issue_pk = view.kwargs['issue_pk']
            issue = get_object_or_404(Issue, pk=issue_pk)
            return request.user in issue.project.contributors.all()

        return False

    def has_object_permission(self, request, view, obj):
        return request.user in obj.issue.project.contributors.all()
