from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "sns"

urlpatterns = [
    path('', views.list, name="posting_list"),
    path('create/', views.create_posting, name="create_posting"),
    path('create/comment/', views.create_comment, name="create_comment"),
    path('delete/', views.delete_posting, name="delete_posting"),
    path('<int:posting_id>/detail/', views.posting_detail, name="posting_detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)