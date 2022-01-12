from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext as _
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique = True )
    is_admin = models.BooleanField(_("Is this user an admin?"), default=False)
    is_manager = models.BooleanField(_("Is this the manager of a store?"), default=False)
    is_active= models.BooleanField(_("Has this user been activated?"), default=True)
    date_joined = models.DateTimeField(_("When did this user join?"), default=timezone.now)
    is_staff = models.BooleanField((""), default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)