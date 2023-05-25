from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# import json

from datos.models import Alumno

@api_view(['GET'])
def graficoStatusCarreraView(request):
    if request.method == 'GET':        
        respuesta = {
            "autorizado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'TELEMATICA').count()
            ],
            "concluido":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'TELEMATICA').count()
            ],
            "corregir_info":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'TELEMATICA').count()
            ],
            "rechazado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'TELEMATICA').count()
            ],
            "reprobado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'TELEMATICA').count()
            ],
            "solicitud":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'AUTOMOTRIZ').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'MANUFACTURA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'MECATRONICA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'NEGOCIOS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'PYMES').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'PYMES EJECUTIVA').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'SISTEMAS').count(),
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'TELEMATICA').count()
            ],
        }
        return Response( respuesta, status= status.HTTP_200_OK)