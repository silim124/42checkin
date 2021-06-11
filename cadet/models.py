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
