from django.db import models
from django.utils import timezone
from .managers import SoftDeletionManager
from django.utils.translation import ugettext_lazy as _


class SoftDeleteMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()

    def delete(self):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    class Meta:
        abstract = True