from rest_framework import permissions

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to admin users
        return request.user and request.user.is_staff