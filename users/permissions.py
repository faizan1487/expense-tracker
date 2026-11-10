from rest_framework.permissions import BasePermission

ROLES = ["Admins"]


class AdminPermission(BasePermission):
    """
    Global permission check for admin users.
    """
    def in_group(self, user):
        return user.groups.filter(name__in=ROLES).exists()

    def has_permission(self, request, view):
        return self.in_group(request.user)
