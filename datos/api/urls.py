from django.contrib import admin
from django.urls import path,include
from .views.encuestaViews import encuesta_detail_view

urlpatterns = [
    path('datos/',include('datos.api.routers')),
    path('datos/encuestaAlumno/<str:pk>/', encuesta_detail_view, name='encuesta_api'),
]