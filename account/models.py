from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import DateTimeField

from common.models.soft_delete_mixin import SoftDeleteModelMixin

__all__ = [
    "UserManager", "User",
]


class UserManager(BaseUserManager):
    def create_user(self, name, is_active=True, **extra_fields):
        user = self.model(name=name, **extra_fields)
        user.is_admin = False
        user.is_staff = False
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password=None):
        user = self.model()
        user.name = name
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, SoftDeleteModelMixin):

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    name = models.CharField(
        max_length=128,
        db_index=True,
        verbose_name="인트라 id",
        primary_key=True,
        unique=True)

    is_staff = models.BooleanField(
        verbose_name="관리자 여부",
    )

    is_superuser = models.BooleanField(
        verbose_name="최고권한 관리자 여부",
    )

    create_time = DateTimeField(
        auto_now_add=True,
        verbose_name="최초 로그인 일시",
    )

    token = models.CharField(
        default="",
        max_length=256
    )

    @property
    def is_active(self) -> bool:
        return self.delete_time is None

    def delete(self, using=None, keep_parents=False):
        SoftDeleteModelMixin.delete(self, using=using, keep_parents=keep_parents)
