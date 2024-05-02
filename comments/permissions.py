from rest_framework import permissions
from issues.models import Issue


class IsContributorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        issue_id = request.parser_context['kwargs'].get('issue_pk')
        issue = Issue.objects.get(pk=issue_id)
        return request.user in issue.assignees.all()

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.issue.assignees.all()
        return obj.author == request.user
