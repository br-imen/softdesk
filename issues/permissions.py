from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    only allow authors of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user

class IsContributorOrAuthor(permissions.BasePermission):
    """
    only allow contributors of a project to view or create,
    and only the author can update or delete.
    """
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.contributors.all() or request.user == obj.author
        return obj.author == request.user
