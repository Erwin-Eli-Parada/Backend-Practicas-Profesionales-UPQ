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
from reportlab.lib import colors, fonts
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from django.db.models import Sum


from datos.models import Empresa

@csrf_exempt
@api_view(['GET'])
def documentoEmpresasView(request):
     # Datos de ejemplo para la tabla

        #datos
        data = [["NOMBRE DE LA EMPRESA","SECTOR","GIRO"]]
        empresas = Empresa.objects.order_by('nombre_empresa')

        for empresa in empresas:
            nombreEmpresa =""
            sector=""

            if(len(empresa.nombre_empresa)>40 and len(empresa.nombre_empresa)<80):
                nombreEmpresa=empresa.nombre_empresa[0:40]+"\n"+empresa.nombre_empresa[41:len(empresa.nombre_empresa)-1]
            elif(len(empresa.nombre_empresa)>=80):
                nombreEmpresa=empresa.nombre_empresa[0:40]+"\n"+empresa.nombre_empresa[41:80]+"\n"+empresa.nombre_empresa[81:len(empresa.nombre_empresa)-1]
            elif(len(empresa.nombre_empresa)<=40):
                nombreEmpresa=empresa.nombre_empresa

            if len(empresa.sector)<=30:
                 sector = empresa.sector
            elif len(empresa.sector)>30:
                 sector = empresa.sector[0:30]+"\n"+empresa.sector[31:len(empresa.sector)-1]
                 
            data.append([nombreEmpresa,sector,empresa.giro])
                 

        # Crear el objeto de respuesta del ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte.pdf"'

        # Crear el documento PDF con ReportLab
        doc = SimpleDocTemplate(response, pagesize=letter)

        # Crear estilos para el texto
        styles = getSampleStyleSheet()
        title_style = styles['Title']
        # paragraph_style = styles['Normal'] 

        # Agregar el título al documento
        title = Paragraph("Reporte de las empresas que reciben practicas profesionales de la Universidad Politécnica de Querétaro", title_style)
        content = [title, Spacer(1, 12)]

        # Agregar la imagen al documento
        image_path = 'datos/UPQlogo.jpg'  # Ruta a la imagen
        image = Image(image_path, width=400, height=200)
        content.append(image)
        content.append(Spacer(1, 24))

        # Agregar un párrafo al documento
        paragraph_text = "Los datos de las empresas que reciben practicas profesionales del periodo mayo a agosto 2021 son los siguientes:" 
        paraStyle = ParagraphStyle(
            name='MiEstilo',
            parent=styles['Normal'],  
            fontSize=14,
            leading=20
        )
        paragraph = Paragraph(paragraph_text, style=paraStyle)
        content.append(paragraph)
        content.append(Spacer(2, 24))

        # Agregar la tabla al documento
        table = Table(data)
        style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),  # Fondo de la primera fila
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),  # Color del texto de la primera fila
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")
        ])
        table.setStyle(style)
        content.append(table)

        # Construir el contenido del documento
        doc.build(content)

        return response