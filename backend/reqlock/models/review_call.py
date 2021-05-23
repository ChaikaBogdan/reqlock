from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from .contract import Contract


class ReviewCall(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name="+")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #TODO: MOVE ROLES TO NEW ORG MODEL
    ROLES = [
        ('QA', _('QA')),
        ('DEV', _('Developer')),
        ('MAN', _('Manager')),
        ('DIR', _('Director')),
        ('SRE', _('SRE')),
        ('DEVOPS', _('DevOps')),
        ('DESIGN', _('Designer')),
        ('PO', _('Projects owner')),

    ]
    SIGN_STATUSES = [
        ('SIGNED', _('Signed')),
        ('AWAIT', _('Requested to sign')),
        ('REJECT', _('Reject to sign')),
        ('NAN', _('Sign not required')),
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
        return _('%(email)s reviews') % {'email': self.user.email}
