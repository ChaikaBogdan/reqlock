from django.db import models

from .component import Component


class Contract(models.Model):
    TYPES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('DESIGN', 'Design'),
    ]
    LOCK_STATUSES = [
        ('LOCK', 'Locked'),
        ('UNLOCK', 'Unlocked'),
        ('AWAIT', 'Awaiting'),

    ]
    CONTRACT_STATUTES = [
        ('DRAFT', 'Draft'),
        ('DESIGN', 'In Design'),
        ('QA', 'QA'),
        ('DEV', 'DEV'),

    ]

    TESTS_STATUSES = [
        ('FAIL', 'Failing'),
        ('PASS', 'Passing'),
        ('FLAKY', 'Unstable'),
        ('NONE', 'None'),
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
