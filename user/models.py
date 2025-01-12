from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_superuser=True)
        user.set_password(password)
        user.save()
        return user

class User(AbstractUser):
    """docstring for User"""
    email               = models.EmailField(verbose_name='Email Address', unique=True)
    name                = models.CharField(max_length=50)
    Coins               = models.DecimalField(decimal_places=2, max_digits= 9, default=100000)
    alert               = models.CharField(max_length=100, default='', null=True, blank=True)
    is_teacher          = models.BooleanField(default=False)
    is_student          = models.BooleanField(default=False)
    is_company          = models.BooleanField(default=False)

    USERNAME_FIELD      = 'email'
    user_permissions    = None
    groups              = None
    REQUIRED_FIELDS     = []

    objects = CustomUserManager()

    def __str__(self):
        return self.name
