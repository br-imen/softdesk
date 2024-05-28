from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """
    only allow authors of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the author of the object.
        return obj.author == request.user


class ContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create,
    and only the author can update or delete.
    """

    def has_object_permission(self, request, view, obj):
        return request.user in obj.contributors.all()


class AuthorOrContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create,
    and only the author can update or delete.
    """

    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.user in obj.contributors.all()
        )
