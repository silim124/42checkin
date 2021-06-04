from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models import DateTimeField


__all__ = ["SoftDeleteModelMixin"]


class SoftDeleteModelMixin(models.Model):
    class Meta:
        abstract = True

    delete_time = DateTimeField(null=True, db_index=True, verbose_name="삭제일시")

    # 삭제 플래그만 삽입해 삭제를 마킹
    def delete(self, using=None, keep_parents=False):
        self.delete_time = datetime.now(tz=settings.TIME_ZONE)
        super(SoftDeleteModelMixin, self).save(using=using)
