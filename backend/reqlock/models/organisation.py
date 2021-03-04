from django.conf import settings
from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    homepage = models.URLField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='+')

    def __str__(self):
        return self.name
