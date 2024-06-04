from rest_framework import permissions
from django.shortcuts import get_object_or_404
from project.models import Project

class AuthorPermission(permissions.BasePermission):
    """
    only allow authors of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user


class ContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create
    """
    def has_permission(self, request, view):
        if 'project_pk' in view.kwargs:
            project = get_object_or_404(Project, pk=view.kwargs['project_pk'])
            return request.user in project.contributors.all()
        return False

    def has_object_permission(self, request, view, obj):
        return request.user in obj.project.contributors.all()


class AuthorOrContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create,
    and only the author can update or delete.
    """

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user in obj.project.contributors.all()
        )


class AssigneesPermission(permissions.BasePermission):
    """
    Permission to only allow assignees of an issue to modify its status,
    """

    def has_object_permission(self, request, view, obj):
        # Allow the author to perform any updates or delete
        return request.user == obj.assignee


class AuthorOrAssigneesPermission(permissions.BasePermission):
    """
    Permission to only allow assignees of an issue to modify its status,
    and the author to update or delete the issue.
    """

    def has_object_permission(self, request, view, obj):
        # Allow the author to perform any updates or delete
        return obj.author == request.user or request.user == obj.assignee
