from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
# Create your models here.
#settings.py => AUTH_USER_MODEL = 'accouts.User'

class User(AbstractUser):
    # username, password, first_name, last_name, email
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers', blank=True)

    def __str__(self):
        return f'{self.username}'