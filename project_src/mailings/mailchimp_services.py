from typing import Optional

from mailchimp3 import MailChimp
from django.conf import settings


def add_mailchimp_email_with_tag(audience_name: str, email: str, tag: str) -> None:
    """Добавляет в MailChimp email в аудиторию с идентификатором audience_name"""

    _add_email_to_mailchimp_audience(
        audience_name=settings.MAILCHIMP_AUDIENCES.get(audience_name),
        email=email
    )

    _add_mailchimp_tag(
        audience_name=audience_name,
        subscriber_hash=_get_mailchimp_subscriber_hash(email),
        tag=tag
    )


def _get_mailchimp_client():
    """Возвращает клиент API для работы с MailChimp"""
    print(f"{settings.MAILCHIMP_USERNAME=}")
    return MailChimp(mc_user=settings.MAILCHIMP_USERNAME,
                     mc_api=settings.MAILCHIMP_APIKEY,
                     )


def _add_email_to_mailchimp_audience(audience_name: str, email: str) -> None:
    mc_client = _get_mailchimp_client()

    mc_client.lists.members.create(audience_name, {
        "email_address": email,
        "status": "subscribed",
    })


def _get_mailchimp_subscriber_hash(email: str) -> Optional[str]:
    """Возвращает идентификатор email'a в MailChamp или None, если email там не найден"""
    mc_client = _get_mailchimp_client()

    members = mc_client \
        .search_members \
        .get(query=email, fields="exact_matches.members.id") \
        .get("exact_matches").get("members")

    if not members:
        return None
    else:
        return members[0].get("id")


def _add_mailchimp_tag(audience_name: str, subscriber_hash: str, tag: str) -> None:
    """Добавляет тэг tag для email'а с идентификатором subscriber_hash в аудитории audience_name"""
    mc_client = _get_mailchimp_client()

    mc_client.lists.members.tags.update(
        list_id=audience_name,
        subscriber_hash=subscriber_hash,
        data={"tags": [{"name": tag, "status": "active"}]}
    )
