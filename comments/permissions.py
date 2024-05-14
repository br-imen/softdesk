from rest_framework import permissions


class ContributorPermission(permissions.BasePermission):
    """
    only allow contributors of a project to view or create,
    and only the author can update or delete.
    """
    def has_object_permission(self, request, view, obj):
        print(obj.issue.project.contributors.all())
        print(request.user)
        return request.user in obj.issue.project.contributors.all()




