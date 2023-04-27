from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('datos/',include('datos.api.routers'))
]