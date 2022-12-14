from rest_framework import permissions
from rest_framework.views import Request, View
from tickets.models import Ticket

from .models import Comment


class IsOwnerOrFromComment(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: View,
        comment: Comment,
    ):
        return request.user.id == comment.user_id or request.user.is_superuser


class isSameDepartamentOrOwnerTicket(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view: View,
    ):
        ticket_id = view.kwargs.get("ticket_id", None)
        ticket_obj = Ticket.objects.get(id=ticket_id)

        return (
            request.user.support_department_id == ticket_obj.support_department_id
            or request.user.id == ticket_obj.owner_id
            or request.user.is_superuser
        )
