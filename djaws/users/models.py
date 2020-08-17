from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.models import AbstractAudit


class User(AbstractUser, AbstractAudit):
    """
    Stores a single user entry, inherence to :model:`auth.AbstractUser`
    """

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
