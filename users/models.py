from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User (AbstractBaseUser
            ):
    email = models.EmailField(unique=True)
    is_active= models.BooleanField(default=True)
    USERNAME_FIELD = 'email'


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


