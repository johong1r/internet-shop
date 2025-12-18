from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager

class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone_number = PhoneNumberField(null=True, blank=True, unique=True, verbose_name='Номер телефона')
   
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{str(self.email) or (self.first_name)}'