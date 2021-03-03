from django.conf import settings
from django.db import models

from .contract import Contract


class Review(models.Model):
    contracts = models.ManyToManyField(Contract, blank=True,related_name='+')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLES = [
        ('QA', 'QA'),
        ('DEV', 'Developer'),
        ('MAN', 'Manager'),
        ('DIR', 'Director'),
        ('SRE', 'SRE'),
        ('DEVOPS', 'DevOps'),
        ('DESIGN', 'Designer'),
        ('PO', 'Projects owner'),

    ]
    SIGN_STATUSES = [
        ('SIGNED', 'Signed'),
        ('AWAIT', 'Requested to sign'),
        ('REJECT', 'Reject to sign'),
        ('NAN', 'Sign not required'),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLES,
        null=True,
        blank=True
    )
    sign_status = models.CharField(
        max_length=50,
        choices=SIGN_STATUSES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user.email} reviews'
