from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class TimeStamp(models.Model):
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True, null=True)

    class Meta:
        abstract = True


class UUIDpk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,)

    class Meta:
        abstract = True


class DefaultModel(TimeStamp, UUIDpk):
    class Meta:
        abstract = True


class ConstModel(TimeStamp):
    class ConstModelManager(models.Manager):
        def get_by_natural_key(self, name):
            return self.get(name=name)

    name = models.CharField(max_length=50)
    objects = ConstModelManager

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
