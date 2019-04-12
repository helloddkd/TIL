from django.db import models
from faker import Faker
# pip install django_rest_framework
faker = Faker()

class Movie(models.Model):
    title = models.CharField(max_length=100)
    @classmethod
    def dummy(cls, n=10):
        for _ in range(n):
            cls.objects.create(title=faker.catch_phrase())
