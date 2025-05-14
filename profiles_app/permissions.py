from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Handles updating own profile"""

    def has_object_permission(self, request, view, obj):
        """checks if the user is updating own prodile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnPostFeed(permissions.BasePermission):
    """Handles updating own post feed"""

    def has_object_permission(self, request, view, obj):
        """Checks if the user is updating own post feed"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author.id == request.user.id
