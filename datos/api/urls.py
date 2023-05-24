from django.contrib import admin
from django.urls import path,include
from .views.encuestaViews import encuesta_detail_view
from .views.graficoStatusView import graficoStatusView
from .views.graficoTipoView import graficoTipoView
from .views.graficoCarreraView import graficoCarreraView

urlpatterns = [
    path('datos/',include('datos.api.routers')),
    path('datos/encuestaAlumno/<str:pk>/', encuesta_detail_view, name='encuesta_api'),
    path('grafico/status/', graficoStatusView, name='grafico_status'),
    path('grafico/tipo/', graficoTipoView, name='grafico_tipo'),
    path('grafico/carrera/', graficoCarreraView, name='grafico_carrera'),
]