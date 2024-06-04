from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # For actions that relate to a specific existing object
        return request.user.id == view.kwargs['pk']

    def has_object_permission(self, request, view, obj):
        if 'pk' in view.kwargs:
            return request.user.id == view.kwargs['pk']
        return False
