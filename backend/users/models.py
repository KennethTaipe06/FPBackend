from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin  
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("First Name"), max_length=150)
    last_name = models.CharField(_("Last Name"), max_length=150)
    email = models.EmailField(_("Email Address"), unique=True)
    is_staff = models.BooleanField(_("Staff Status"), default=False)
    is_active = models.BooleanField(_("Active Status"), default=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta: 
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"    

