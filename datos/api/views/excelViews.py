from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datos.models import AsesorUPQ
from datos.models import Empresa
from datos.models import AsesorExterno
from datos.models import EstatusResidencia
from datos.api.serializers.asesorUPQSerializer import AsesorUPQIdSerializer, AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer
import pandas as pd
import math

class ExcelViewSet(viewsets.ModelViewSet):
    def create(self,request):
        archivo = request.FILES.get('archivo')
        data = pd.read_excel(archivo)
        df = pd.DataFrame(data)
        id_asesorupq = 1
        id_asesor = 1
        id_empresa = 1

        
        for i in range(len(data)):
            #Datos del Asesor UPQ
            if str(df.at[i, 'Asesor UPQ']) != "nan":
                if not AsesorUPQ.objects.filter(nombre=str(df.at[i, 'Asesor UPQ'])).exists():
                    dataR = {"nombre":str(df.at[i, 'Asesor UPQ'])}
                    serializer = AsesorUPQSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
                        # asesorupq = asesorupq + str(df.at[i, 'Asesor UPQ']) +"\n"

                # print(str(id_asesorupq))

            #Datos de la Empresa
            if str(df.at[i,'Empresa']) != "nan":
                if not Empresa.objects.filter(nombre_empresa=str(df.at[i, 'Empresa'])).exists():
                    dataR = {
                        "nombre_empresa":str(df.at[i, 'Empresa']),
                        "sector":str(df.at[i, 'Sector']),
                        "giro":str(df.at[i, 'Giro']),
                        "tamanio":"" if str(df.at[i, 'Tamaño']) == "nan" else str(df.at[i, 'Tamaño']),
                        "correo":str(df.at[i, 'Correo RH Empresa']),
                        "telefono":str(df.at[i, 'Telefono RH Empresa'])
                    }
                    serializer = EmpresaSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(dataR['tamanio'],status = status.HTTP_400_BAD_REQUEST)    

            #Datos del Asesor Externo
            if str(df.at[i, 'Asesor Empresa']) != "nan":
                if not AsesorExterno.objects.filter(nombre_asesor_ext=str(df.at[i, 'Asesor Empresa'])).exists():
                    dataR = {"nombre_asesor_ext":str(df.at[i, 'Asesor Empresa'])}
                    serializer = AsesorExternoSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

            #Datos de Estatus de la residencia
            if str(df.at[i, 'Id']) != "nan":
                if not EstatusResidencia.objects.filter(id_practica=str(df.at[i, 'Id'])).exists():
                    dataR = {
                        "id_practica":str(df.at[i, 'Id']),
                        "comentarios_status":str(df.at[i, 'Comentario Estatus']),
                        "estatus_proceso":str(df.at[i, 'Estatus Proceso']),
                        "tipo_proceso": str(df.at[i, 'Tipo proceso']),
                        "carta_recibida": True if str(df.at[i, 'Recibio Carta']) == "SI" else False,
                        "avance_1":True if str(df.at[i, 'Avance 1']) == "SI" else False,
                        "avance_2":True if str(df.at[i, 'Avance 2']) == "SI" else False,
                        "reporte_final":True if str(df.at[i, 'Reporte Final']) == "SI" else False,
                        "carta_liberacion":True if str(df.at[i, 'Carta liberacion']) == "SI" else False
                    }
                    serializer = EstatusSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

                #Datos del proyecto
                asesor = AsesorUPQIdSerializer.Meta.model.objects.filter(nombre=str(df.at[i, 'Asesor UPQ'])).first()
                if asesor is not None:
                    id_asesorupq = asesor.id_asesor

                

        # serializer = ProyectoCrearSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'mensaje':'Alumno creado correctamente!'}, status = status.HTTP_201_CREATED)   
        # return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje':'Agregado correctamente'}, status = status.HTTP_201_CREATED)  