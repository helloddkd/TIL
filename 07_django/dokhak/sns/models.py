from django.db import models

# Create your models here.


class Posting(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    image = models.ImageField(blank=True, null=True)


class Comment(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)

