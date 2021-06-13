from django.conf import settings
from django.db import models
from .contract import Contract
from .sign_status import SignStatus
from .ogranisation_role import OrganisationRole
from .model_mixins import SoftDeleteModel
from django.utils.translation import gettext_lazy as _


class ReviewCall(SoftDeleteModel):
    contract = models.ForeignKey(Contract, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.DO_NOTHING)

    role = models.ForeignKey(OrganisationRole, on_delete=models.DO_NOTHING)
    sign_status = models.ForeignKey(SignStatus, on_delete=models.DO_NOTHING)

    def __str__(self):
        return _('Review from {email} in status "{sign_status}"').format(
            email=self.user.email,
            sign_status=self.sign_status or _('Unknown'),
        )
