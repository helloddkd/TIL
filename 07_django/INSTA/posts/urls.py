from . import views
from django.urls import path

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('create/', views.create_post, name="create_post"),
    path('<int:post_id>/update/', views.update_post, name="update_post"),
    path('<int:post_id>/delete/', views.delete_post, name="delete_post"),
    path('<int:post_id>/comment', views.create_comment, name="create_comment"),
    path('<int:post_id>/comment/<int:comment_id>/', views.delete_comment, name="delete_comment")
]
