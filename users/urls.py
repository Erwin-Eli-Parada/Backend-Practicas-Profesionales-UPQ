from django.urls import path
from .api import user_api_view, user_detail_view, user_login_view

urlpatterns = [
    path('api/usuario/', user_api_view, name='usuario_api'),
    path('api/usuario/<str:correo>/<str:password>/', user_login_view, name="usuario_login_view"),
    path('api/usuario/<int:pk>/', user_detail_view, name="usuario_detail_view")
]