from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_extensions.db.models import TimeStampedModel
import os
from django.conf import settings
from django.contrib.auth.models import User

ENV = os.environ.get('ENVIRONMENT', 'development')
if ENV == 'development':
    from IPython import embed
    from faker import Faker
faker = Faker()
# Create your models here.


class Post(TimeStampedModel):
    content = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    #배포시엔 삭제
    @classmethod
    def dummy(cls, n=10):
        for i in range(n):
            Post.objects.create(content=faker.text(120))

class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        blank=True,
        upload_to='posts/images',
        processors=[ResizeToFill(600,600)],
        format='JPEG',
        options={'quality': 90}
    )

class Comment(TimeStampedModel):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
