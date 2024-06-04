from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create
    """
    def has_permission(self, request, view):
        # For actions that relate to a specific existing object
        print(view.kwargs['pk'])
        print(request.user.id == view.kwargs['pk']  )
        return request.user.id == view.kwargs['pk']

    def has_object_permission(self, request, view, obj):
        print("has_object_permission", view.kwargs['pk'])
        if 'pk' in view.kwargs:
            return request.user.id == view.kwargs['pk']
        return False
