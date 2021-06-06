from django.db import models

from account.models import User

__all__ = [
    "CadetUser",
]


class CadetUser(User):
    class Meta:
        proxy = True
        verbose_name = "카뎃"
        verbose_name_plural = "카뎃들"

    social_token = models.CharField(max_length=128)
    token = models.CharField(max_length=256)
