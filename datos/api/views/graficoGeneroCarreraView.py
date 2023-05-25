from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoGeneroCarreraView(request):
    if request.method == 'GET':        
        respuesta = {
            "hombre":[
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(genero = 'MASCULINO').filter(carrera = 'TELEMATICA').count()
            ],
            "mujer":[
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(genero = 'FEMENINO').filter(carrera = 'TELEMATICA').count()
            ]
        }
        return Response( respuesta, status= status.HTTP_200_OK)