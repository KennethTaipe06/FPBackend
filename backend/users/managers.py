from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email"))
        
    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Base User: an email address is required"))
        if not first_name:
            raise ValueError(_("Users must submit a first name"))
        if not last_name:
            raise ValueError(_("Users must submit a last name"))

        email = self.normalize_email(email)
        self.email_validator(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        
        if not password:
            raise ValueError(_("Superusers must have a password"))

        user = self.create_user(first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)   

        return user