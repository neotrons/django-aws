from django.contrib.auth.base_user import BaseUserManager


class CoreManager(BaseUserManager):
    def actives(self):
        return super(CoreManager, self).get_queryset().filter(is_active=True)
