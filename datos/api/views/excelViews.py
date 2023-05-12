from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from datos.models import AsesorUPQ
from datos.models import Empresa
from datos.models import AsesorExterno
from datos.models import EstatusResidencia
from datos.models import Alumno
from datos.api.serializers.asesorUPQSerializer import AsesorUPQIdSerializer, AsesorUPQSerializer
from datos.api.serializers.empresaSerializer import EmpresaSerializer, EmpresaIdSerializer
from datos.api.serializers.asesorExternoSerializer import AsesorExternoSerializer, AsesorExternoIdSerializer
from datos.api.serializers.estatusSerializer import EstatusSerializer
from datos.api.serializers.proyectoSerializer import ProyectoCrearSerializer, ProyectoIdSerializer
from datos.api.serializers.alumnoSerializer import AlumnoCrearSerializer
import pandas as pd
import math

class ExcelViewSet(viewsets.ModelViewSet):
    def create(self,request):
        archivo = request.FILES.get('archivo')
        data = pd.read_excel(archivo)
        df = pd.DataFrame(data)
        
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
                    id_asesorupq = 1
                    id_asesor = 1
                    id_empresa = 1

                    asesor = AsesorUPQIdSerializer.Meta.model.objects.filter(nombre=str(df.at[i, 'Asesor UPQ'])).first()
                    if asesor is not None:
                        id_asesorupq = asesor.id_asesor

                    asesorext = AsesorExternoIdSerializer.Meta.model.objects.filter(nombre_asesor_ext=str(df.at[i, 'Asesor Empresa'])).first()
                    if asesorext is not None:
                        id_asesor = asesorext.id_asesor_ext

                    empresa = EmpresaIdSerializer.Meta.model.objects.filter(nombre_empresa=str(df.at[i, 'Empresa'])).first()
                    if empresa is not None:
                        id_empresa = empresa.id_empresa

                    dataR2 ={
                        "id_practica":str(df.at[i, 'Id']),
                        "nombre_proyecto":str(df.at[i, 'Proyecto']),
                        "fecha_solicitud":"0001-01-01 00:00:01" if str(df.at[i, 'Fecha Solicitud'])=="nan" else str(df.at[i, 'Fecha Solicitud']),
                        "metodo_conocimiento":str(df.at[i, 'Metodo conocimiento']),
                        "calificacion": 0 if str(df.at[i, 'Calificación Final']) == "nan" else df.at[i, 'Calificación Final'],
                        "comentarios_finales":str(df.at[i, 'Comentarios Finales']),
                        "id_asesor":id_asesorupq,
                        "id_empresa":id_empresa,
                        "id_asesor_ext":id_asesor
                    }

                    serializer2 = ProyectoCrearSerializer(data = dataR2)
                    if serializer2.is_valid():
                        serializer2.save()
                    else:
                        # return Response(dataR2["id_practica"]+" "+str(dataR2["fecha_solicitud"]),status = status.HTTP_400_BAD_REQUEST)
                        return Response(serializer2.errors,status = status.HTTP_400_BAD_REQUEST)
                    
                    print("asesor upq "+ str(id_asesorupq)+" asesor externo "+str(id_asesor)+" empresa "+str(id_empresa))

            if str(df.at[i, 'Matricula']) != "nan":
                if not Alumno.objects.filter(matricula=str(df.at[i, 'Matricula'])).exists():

                    id_practica = 1

                    proyecto = ProyectoIdSerializer.Meta.model.objects.filter(id_practica=str(df.at[i, 'Id'])).first()
                    if proyecto is not None:
                        id_practica = proyecto.id
                        
                    dataR={
                        "matricula":df.at[i, 'Matricula'],
                        "correo":str(df.at[i, 'Correo']),
                        "correo_institucional":str(df.at[i, 'Correo Institucional']),
                        "generacion":str(df.at[i, 'Generación']),
                        "grupo":str(df.at[i, 'Grupo']),
                        "carrera":str(df.at[i, 'Carrera']),
                        "nss":str(df.at[i, 'NSS']),
                        "genero":str(df.at[i, 'Genero']),
                        "nombre":str(df.at[i, 'Alumno']),
                        "id_practica":id_practica
                    }

                    serializer = AlumnoCrearSerializer(data = dataR)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(dataR["matricula"]+" "+str(dataR["correo"]) +" "+ str(dataR["correo_institucional"]) ,status = status.HTTP_400_BAD_REQUEST)
                        # return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 
                

        # serializer = ProyectoCrearSerializer(data = request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({'mensaje':'Alumno creado correctamente!'}, status = status.HTTP_201_CREATED)   
        # return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        return Response({'mensaje':'Agregado correctamente'}, status = status.HTTP_201_CREATED)  