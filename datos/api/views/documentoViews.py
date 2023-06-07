from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters
from datos.api.serializers.alumnoSerializer import AlumnoSerializer
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from django.db.models import Sum


from datos.models import Alumno
from datos.models import Encuesta

@csrf_exempt
@api_view(['GET'])
def documentoView(request):
     # Datos de ejemplo para la tabla
        #Procesos
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
        
        #Carreras
        automotriz = 0
        manufactura = 0
        mecatronica = 0
        negocios = 0
        pymes = 0
        pymes_eje = 0
        sistemas = 0
        telematica = 0

        automotriz = Alumno.objects.filter(carrera = 'AUTOMOTRIZ').count()
        manufactura = Alumno.objects.filter(carrera = 'MANUFACTURA').count()
        mecatronica = Alumno.objects.filter(carrera = 'MECATRONICA').count()
        negocios = Alumno.objects.filter(carrera = 'NEGOCIOS').count()
        pymes = Alumno.objects.filter(carrera = 'PYMES').count()
        pymes_eje = Alumno.objects.filter(carrera = 'PYMES EJECUTIVA').count()
        sistemas = Alumno.objects.filter(carrera = 'SISTEMAS').count()
        telematica = Alumno.objects.filter(carrera = 'TELEMATICA').count()

        if automotriz == None or manufactura==None or mecatronica==None or negocios==None or pymes==None or pymes_eje==None or sistemas==None or telematica==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        #Status carreras
        estatus_carreras = {
            "autorizado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'AUTORIZADO').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
            "concluido":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
            "corregir_info":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'CORREGIR INFORMACIÓN').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
            "rechazado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'RECHAZADO').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
            "reprobado":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'REPROBADO').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
            "solicitud":[
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'AUTOMOTRIZ').count()*100/automotriz,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'MANUFACTURA').count()*100/manufactura,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'MECATRONICA').count()*100/mecatronica,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'NEGOCIOS').count()*100/negocios,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'PYMES').count()*100/pymes,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'PYMES EJECUTIVA').count()*100/pymes_eje,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'SISTEMAS').count()*100/sistemas,
                Alumno.objects.filter(id_practica__id_practica__estatus_proceso = 'SOLICITUD').filter(carrera = 'TELEMATICA').count()*100/telematica
            ],
        }

        #tipo
        estadiaTotal = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estadia').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estadiaSuma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estadia').aggregate(total=Sum('id_practica__calificacion'))['total']

        estancia1Total = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia I').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estancia1Suma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia I').aggregate(total=Sum('id_practica__calificacion'))['total']

        estancia2Total = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia II').filter(id_practica__id_practica__estatus_proceso = 'CONCLUIDO').count()
        estancia2Suma = Alumno.objects.filter(id_practica__id_practica__tipo_proceso = 'Estancia II').aggregate(total=Sum('id_practica__calificacion'))['total']

        #contrato
        siContrato = Alumno.objects.filter(id_practica__id_asesor_ext__encuesta__valor_descripcion="SI").filter(id_practica__id_asesor_ext__encuesta__pregunta="¿El alumno será contratado al término de su Estadia?").filter(id_practica__id_practica__tipo_proceso = 'Estadia').count()

        noContrato = Alumno.objects.filter(id_practica__id_asesor_ext__encuesta__valor_descripcion="NO").filter(id_practica__id_asesor_ext__encuesta__pregunta="¿El alumno será contratado al término de su Estadia?").filter(id_practica__id_practica__tipo_proceso = 'Estadia').count() 

        totalContrato = siContrato+noContrato

        #datos
        data = [
            ['Cantidad de procesos autorizados:', autorizado],             #procesos
            ['Cantidad de procesos concluidos:', concluido],
            ['Cantidad de procesos con información por corregir:', corregir_info],
            ['Cantidad de procesos en solicitud', solicitud],
            ['Cantidad de procesos rechazados', rechazado],
            ['Cantidad de procesos reprobados', reprobado],
            ['Cantidad de alumnos en la carrera de Automotriz', automotriz],  #automotriz
            ['Porcentaje del estatus autorizado en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['autorizado'][0]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['concluido'][0]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['corregir_info'][0]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['rechazado'][0]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['reprobado'][0]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Automotriz', str("{:.2f}".format(estatus_carreras['solicitud'][0]))+"%"],
            ['Cantidad de alumnos en la carrera de Manufactura', manufactura], #manufactura
            ['Porcentaje del estatus autorizado en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['autorizado'][1]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['concluido'][1]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['corregir_info'][1]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['rechazado'][1]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['reprobado'][1]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Manufactura', str("{:.2f}".format(estatus_carreras['solicitud'][1]))+"%"],
            ['Cantidad de alumnos en la carrera de Mecatronica', mecatronica], #mecatronica
            ['Porcentaje del estatus autorizado en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['autorizado'][2]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['concluido'][2]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['corregir_info'][2]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['rechazado'][2]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['reprobado'][2]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Mecatronica', str("{:.2f}".format(estatus_carreras['solicitud'][2]))+"%"],
            ['Cantidad de alumnos en la carrera de Negocios', negocios],    #negocios
            ['Porcentaje del estatus autorizado en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['autorizado'][3]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['concluido'][3]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['corregir_info'][3]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['rechazado'][3]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['reprobado'][3]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Negocios', str("{:.2f}".format(estatus_carreras['solicitud'][3]))+"%"],
            ['Cantidad de alumnos en la carrera de PYMES', pymes],       #pymes
            ['Porcentaje del estatus autorizado en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['autorizado'][4]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['concluido'][4]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['corregir_info'][4]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['rechazado'][4]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['reprobado'][4]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de PYMES', str("{:.2f}".format(estatus_carreras['solicitud'][4]))+"%"],
            ['Cantidad de alumnos en la carrera de PYMES Ejecutiva', pymes_eje],   #pymes eje
            ['Porcentaje del estatus autorizado en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['autorizado'][5]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['concluido'][5]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['corregir_info'][5]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['rechazado'][5]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['reprobado'][5]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de PYMES Ejecutiva', str("{:.2f}".format(estatus_carreras['solicitud'][5]))+"%"],
            ['Cantidad de alumnos en la carrera de Sistemas Computacionales', sistemas],  #sistemas
            ['Porcentaje del estatus autorizado en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['autorizado'][6]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['concluido'][6]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['corregir_info'][6]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['rechazado'][6]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['reprobado'][6]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Sistemas computacionales', str("{:.2f}".format(estatus_carreras['solicitud'][6]))+"%"], 
            ['Cantidad de alumnos en la carrera de Telemática', telematica],    #telematica
            ['Porcentaje del estatus autorizado en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['autorizado'][7]))+"%"],
            ['Porcentaje del estatus concluido en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['concluido'][7]))+"%"],
            ['Porcentaje del estatus correccion de información en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['corregir_info'][7]))+"%"],
            ['Porcentaje del estatus rechazado en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['rechazado'][7]))+"%"],
            ['Porcentaje del estatus reprobado en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['reprobado'][7]))+"%"],
            ['Porcentaje del estatus solicitud en la carrera de Telemática', str("{:.2f}".format(estatus_carreras['solicitud'][7]))+"%"],
            ['Promedio de calificaciones en la Estancia I', str("{:.2f}".format(estancia1Suma/estancia1Total))],   #promedios
            ['Promedio de calificaciones en la Estancia II', str("{:.2f}".format(estancia2Suma/estancia2Total))],
            ['Promedio de calificaciones en la Estadia', str("{:.2f}".format(estadiaSuma/estadiaTotal))],
            ['Porcentaje de alumnos que serán contratados al termino de su Estadia',  str("{:.2f}".format(siContrato*100/totalContrato))+"%"]   #contratos  
        ]

        # Crear el objeto de respuesta del ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

        # Crear el documento PDF con ReportLab
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Crear estilos para el texto
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        paragraph_style = styles['Normal'] 

        # Agregar el título al documento
        title = Paragraph("Reporte de las practicas profesionales de la Universidad Politécnica de Querétaro", title_style)
        content = [title, Spacer(1, 12)]

        # Agregar la imagen al documento
        image_path = 'datos/UPQlogo.jpg'  # Ruta a la imagen
        image = Image(image_path, width=400, height=200)
        content.append(image)
        content.append(Spacer(1, 24))

        # Agregar un párrafo al documento
        paragraph_text = "Las métricas de las practicas profesionales son las siguientes:" 
        paragraph = Paragraph(paragraph_text, paragraph_style)
        content.append(paragraph)
        content.append(Spacer(2, 24))

        # Agregar la tabla al documento
        table = Table(data)
        style = TableStyle([
            # Estilos de la tabla
        ])
        table.setStyle(style)
        content.append(table)

        # Construir el contenido del documento
        doc.build(content)

        return response