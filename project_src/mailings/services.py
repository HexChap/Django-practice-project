from typing import Union

from .mailchimp_services import add_mailchimp_email_with_tag
from .models import CommonMailingsList, CaseMailingsList




def add_to_common_list(email: str):
    """Добавляет email в общий лист рассылки"""
    add_mailchimp_email_with_tag(
        audience_id="COMMON",
        email=email,
        tag="COMMON TAG"
    )

    CommonMailingsList.objects.get_or_create(email=email)


def add_email_to_case_list(email: str, case_id: Union[int, str]):
    """Добавляет email в лист рассылки по делу case"""
    case = Case.objects.get(pk=case_id)
    case_tag = f"CASE {case.name}"

    _add_mailchimp_email_with_tag(
        audience_id="CASES",
        email=email,
        tag=case_tag
    )

    CaseMailingsList.objects.get_or_create(email=email, case=case)
