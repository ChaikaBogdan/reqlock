from django.db import models
from .organisation import Organisation
from .model_mixins import SoftDeleteMixin
from django.utils.translation import ugettext_lazy as _


class LockStatus(SoftDeleteMixin, models.Model):

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Lock status')
        verbose_name_plural = _('Lock statuses')
