from django.db import models
from faker import Faker
# Create your models here.
faker = Faker()


class User(models.Model):
    name = models.CharField(max_length=10)


class Profile(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=30)
    # class Meta:
    #     ordering = ('name',)
    @classmethod
    def dummy_data(cls, n=10):
        for _ in range(n):
            cls.objects.create(name=faker.name())


class Hotel(models.Model):
    name = models.CharField(max_length=30)
    clients = models.ManyToManyField(Client)

    @classmethod
    def dummy_data(cls, n=10):
        for _ in range(n):
            cls.objects.create(name=faker.company())


class Student(models.Model):
    name = models.CharField(max_length=30)


class Lecture(models.Model):
    title = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

