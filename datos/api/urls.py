from django.contrib import admin
from django.urls import path,include
from .views.encuestaViews import encuesta_detail_view
from .views.graficoStatusView import graficoStatusView
from .views.graficoTipoView import graficoTipoView
from .views.graficoCarreraView import graficoCarreraView
from .views.graficoGeneroView import graficoGeneroView
from .views.graficoGiroView import graficoGiroView
from .views.graficoTamanioView import graficoTamanioView
from .views.graficoGeneracionView import graficoGeneracionView
from .views.graficoCalificacionTipoView import graficoCalificacionTipoView
from .views.graficoGeneroCarreraView import graficoGeneroCarreraView

urlpatterns = [
    path('datos/',include('datos.api.routers')),
    path('datos/encuestaAlumno/<str:pk>/', encuesta_detail_view, name='encuesta_api'),
    path('grafico/status/', graficoStatusView, name='grafico_status'),
    path('grafico/tipo/', graficoTipoView, name='grafico_tipo'),
    path('grafico/carrera/', graficoCarreraView, name='grafico_carrera'),
    path('grafico/genero/', graficoGeneroView, name='grafico_genero'),
    path('grafico/giro/', graficoGiroView, name='grafico_giro'),
    path('grafico/tamanio/', graficoTamanioView, name='grafico_tamanio'),
    path('grafico/generacion/', graficoGeneracionView, name='grafico_generacion'),
    path('grafico/calificacionTipo/', graficoCalificacionTipoView, name='grafico_calificacionTipo'),
    path('grafico/generoCarrera/', graficoGeneroCarreraView, name='grafico_generoCarrera'),
]