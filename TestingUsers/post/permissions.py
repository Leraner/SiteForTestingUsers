from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthOrReadOnly(BasePermission):
    def has_permission(self, request, view) -> bool:
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj) -> bool:
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_authenticated and (obj.author == request.user)
        )



