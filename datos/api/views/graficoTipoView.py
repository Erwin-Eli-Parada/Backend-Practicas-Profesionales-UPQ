from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoTipoView(request):
    if request.method == 'GET':
        autorizado = 0
        concluido = 0
        corregir_info = 0
        solicitud = 0
        rechazado = 0
        reprobado = 0

        autorizado = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').count()
        concluido = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        corregir_info = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').count()
        solicitud = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').count()
        rechazado = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').count()
        reprobado = Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').count()

        if autorizado == None or solicitud==None or concluido==None or corregir_info==None or rechazado==None or reprobado==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        respuesta = {
            'autorizado': autorizado,
            'concluido' : concluido,
            'corregir_info': corregir_info,
            'solicitud' : solicitud,
            'rechazado' : rechazado,
            'reprobado' : reprobado
        }
        return Response( respuesta, status= status.HTTP_200_OK)