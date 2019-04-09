from django.contrib import admin
from .models import Article
# Article 모델을 admin site 에서 등록해서 확인할래!

admin.site.register(Article)
