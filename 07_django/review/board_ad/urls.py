from django.urls import path
from . import views



app_name = 'board_ad'

urlpatterns = [
    # Read
    path('', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    # Create
    path('new/', views.posting_create, name='posting_create'),
    # Update
    path('<int:posting_id>/edit/', views.posting_update, name='posting_update'),
    # Delete
    path('<int:posting_id>/delete/', views.posting_delete, name='posting_delete'),

    path('<int:posting_id>/comments/create/', views.create_comment, name="create_comment"),
    path('<int:posting_id>/comments/<int:comment_id>/delete/', views.delete_comment, name="delete_comment"),
    path('<int:posting_id>/comments/<int:comment_id>/update/', views.update_comment, name="update_comment"),
]
