from django.urls import path
from .api import user_api_view, user_detail_view

urlpatterns = [
    path('api/usuario/', user_api_view, name='usuario_api'),
    path('api/usuario/<str:nombre>/', user_detail_view, name="usuario_detail_view")
]