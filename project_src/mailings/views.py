from django.http import JsonResponse
from django.conf import settings

from .services import add_to_common_list, add_email_to_case_list


def add_to_common_view(request):
    """Веб сервис добавляющий email в общий лист рассылки"""
    email = request.GET.get("email")
    if not email:
        return JsonResponse({"success": False, "message": "Передайте email"})

    add_to_common_list(email=email)

    return JsonResponse({"success": True})


def add_to_case_list_view(request):
    """Веб-сервис, добавляющий email в лист рассылком по конкретному делу."""
    email = request.GET.get("email")
    case_id = request.GET.get("case_id")
    if not email:
        return JsonResponse({"success": False, "message": "Передайте email"})
    elif not case_id:
        return JsonResponse({"success": False, "message": "Передайте case_id"})

    add_email_to_case_list(email, case_id)

    return JsonResponse({"success": True})
