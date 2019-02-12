from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='list'),
    path('create/', views.create, name='create'),
    path('<int:movie_id>/update/', views.update, name='update')
]