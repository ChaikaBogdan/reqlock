from django.conf import settings
from django.db import models
from .contract import Contract
from .sign_status import SignStatus
from .company_role import CompanyRole

class ReviewCall(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)

    role = models.ForeignKey(CompanyRole, on_delete=models.CASCADE)
    sign_status = models.ForeignKey(SignStatus, on_delete=models.CASCADE)

    def __str__(self):
        return _('Review from {email} in status "{sign_status}"').format(
            email=self.user.email,
            sign_status=self.sign_status or _('Unknown'),
        )
