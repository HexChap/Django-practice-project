from django.shortcuts import render
from django.http import JsonResponse

from project_src.mailings.mailchimp_services import add_mailchimp_email_with_tag


def webhook(request):
    """Обработчик вебхука от платежной системы"""
    email = request.GET.get("email")
    if not email:
        return JsonResponse({"success": False, "message": "Передайте email"})
    add_mailchimp_email_with_tag(email=email, audience_name="DONATES", tag="DONATE")
