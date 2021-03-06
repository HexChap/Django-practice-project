from django.db import models


class CommonMailingsList(models.Model):
    """Рассылка на общие материалы сайта"""
    email = models.EmailField("Email подписчика")

    class Meta:
        db_table = "common_mailing_list"


class CaseMailingsList(models.Model):
    """Рассылка на материалы конкретного дела"""
    email = models.EmailField("Email подписчика")
    case = models.ForeignKey(to="cases.Case", verbose_name="Дело", on_delete=models.CASCADE)

    class Meta:
        db_table = "case_mailing_list"
