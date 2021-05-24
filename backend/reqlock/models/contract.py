from django.db import models
from django.utils.translation import gettext as _

from .component import Component


class Contract(models.Model):
    # TODO: Should be models related to Organisation with order for statutes
    # TODO: change type and *_status to FKs
    # Please just use 255 for char fields instead of 50-255 it has NO performance impact
    # Lock statuses looks like NULL bolean field Null -await, Unlock -False, lock - True
    TYPES = [
        ('FRONTEND', _('Frontend')),
        ('BACKEND', _('Backend')),
        ('DESIGN', _('Design')),
    ]
    LOCK_STATUSES = [
        ('LOCK', _('Locked')),
        ('UNLOCK', _('Unlocked')),
        ('AWAIT', _('Awaiting')),
    ]
    CONTRACT_STATUTES = [
        ('DRAFT', _('Draft')),
        ('DESIGN', _('In Design')),
        ('QA', _('QA')),
        ('DEV', _('DEV')),
        ('DONE', _('DONE')),
    ]
    TESTS_STATUSES = [
        ('FAIL', _('Failing')),
        ('PASS', _('Passing')),
        ('FLAKY', _('Unstable')),
        ('NONE', _('None')),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=TYPES,
        null=True,
        blank=True
    )
    lock_status = models.CharField(
        max_length=50,
        choices=LOCK_STATUSES,
        null=True,
        blank=True
    )
    contract_status = models.CharField(
        max_length=50,
        choices=CONTRACT_STATUTES,
        null=True,
        blank=True
    )
    tests_status = models.CharField(
        max_length=50,
        choices=TESTS_STATUSES,
        null=True,
        blank=True
    )

    components = models.ManyToManyField(Component, blank=True, related_name='+')

    def __str__(self):
        return self.name
