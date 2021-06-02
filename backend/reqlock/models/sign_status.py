from django.db import models
from .organisation import Organisation
from .model_mixins import SoftDeleteModel
from django.utils.translation import ugettext_lazy as _


class SignStatus(SoftDeleteModel):

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Sign status')
        verbose_name_plural = _('Sign statuses')
