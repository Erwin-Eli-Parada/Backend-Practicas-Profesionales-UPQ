from django.urls import path
from .api import historial_api_view

urlpatterns = [
    path('api/historial/', historial_api_view, name='historial_api')
]