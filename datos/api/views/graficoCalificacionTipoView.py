from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Sum
import json

from datos.models import Alumno

@api_view(['GET'])
def graficoCalificacionTipoView(request):
    if request.method == 'GET':
        
        estadiaTotal = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estadia').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estadiaSuma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estadia').aggregate(total=Sum('id_practica__calificacion'))['total']

        estancia1Total = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia I').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estancia1Suma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia I').aggregate(total=Sum('id_practica__calificacion'))['total']

        estancia2Total = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia II').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estancia2Suma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia II').aggregate(total=Sum('id_practica__calificacion'))['total']

        respuesta = {
            "estadia": estadiaSuma/estadiaTotal if estadiaTotal!=0 else 0,
            "estancia1": estancia1Suma/estancia1Total if estancia1Total!=0 else 0,
            "estancia2": estancia2Suma/estancia2Total if estancia2Total!=0 else 0
        }
        
        return Response(respuesta, status= status.HTTP_200_OK) 