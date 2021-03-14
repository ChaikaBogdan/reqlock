from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from .project import Project


class Component(models.Model):
    #TODO: ADD NEW COPONENT TYPES ADDED TO ORG
    TYPES = [
        ('FRONTEND', _('Frontend')),
        ('BACKEND', _('Backend')),
        ('MONOLITH', _('Monolith')),
        ('LAMBDA', _('Lambda')),
        ('PRODUCER', _('Producer')),
        ('CONSUMER', _('Consumer')),
        ('BROKER', _('Broker')),
        ('QUEUE', _('Queue')),
        ('WORKER', _('Worker')),
        ('DB', _('Database')),
        ('DS', _('Data Source')),
    ]
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tech_stack = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=TYPES,
        null=True, blank=True
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
