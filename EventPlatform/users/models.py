from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User (AbstractBaseUser
            ):
    email = models.EmailField(unique=True)
    is_active= models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_images/', null= True, blank= True)
    prefix = models.CharField(max_length = 10, null =True, blank = True)
    home_address = models.TextField(null=True, blank =True)
    billing_address = models.TextField(null=True, blank =True)

    USERNAME_FIELD = 'email'


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


