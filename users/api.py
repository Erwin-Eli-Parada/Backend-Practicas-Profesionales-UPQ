from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.hashers import check_password
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioAgregarSerializer, UsuarioActualizarSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = Usuario.objects.all()
        users_serializer = UsuarioSerializer(users, many=True)
        return Response(users_serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UsuarioAgregarSerializer(data = request.data)
        if(users_serializer.is_valid()):
            users_serializer.save()
            return Response(users_serializer.data, status= status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_login_view(request,correo=None, password=None):
    user = Usuario.objects.filter(email = correo).first()
    if user==None:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    hashed_password = user.password
    if check_password(password, hashed_password):
    # La contraseña es correcta
        print('Contraseña válida')
        user_serializer = UsuarioSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)
    else:
    # La contraseña es incorrecta
        print('Contraseña incorrecta')
        user_serializer = UsuarioSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk=None):
    if request.method == 'GET':
        user = Usuario.objects.filter(id = pk).first()
        if user==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user_serializer = UsuarioSerializer(user)
        return Response(user_serializer.data, status= status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        user = Usuario.objects.filter(id=pk).first()
        print(request.data)
        user_serializer = UsuarioActualizarSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status= status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user = Usuario.objects.filter(id=pk).first()
        if user==None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response('Eliminado', status= status.HTTP_200_OK)
    
@api_view(['POST'])
def recuperar_contra_view(request):
    if request.method == 'POST':
        correo = request.data.get("correo")
        if correo is not None:
            usuario = Usuario.objects.filter(email=correo).first()

            if usuario is not None:
                caracteres_permitidos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
                cadena = ""
    
                for _ in range(10):
                    caracter_aleatorio = random.choice(caracteres_permitidos)
                    cadena += caracter_aleatorio

                data={'password': cadena, 'last_login': None, 'is_superuser': usuario.is_superuser, 'first_name': '', 'last_name': '', 'is_staff': usuario.is_staff, 'is_active': usuario.is_active, 'date_joined': usuario.date_joined, 'username': usuario.username, 'email': usuario.email, 'nombre': usuario.nombre, 'groups': [], 'user_permissions': []}

                user_serializer = UsuarioActualizarSerializer(usuario, data)
                if user_serializer.is_valid():
                    user_serializer.save()

                smtp_server = 'smtp.gmail.com'
                smtp_port = 587
                sender_email = 'pracpromecatronicaupq@gmail.com'
                sender_password = 'vnqxcvzexejaufld'

                # Crear objeto MIMEMultipart para el correo
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = correo
                msg['Subject'] = 'Recuperación de contraseña'

                # Agregar el cuerpo del mensaje
                mensaje = '¡Hola! Este es un mensaje para recuperar la contraseña. \n\nTu nueva contraseña es la siguiente: '+cadena+'\n\n Si quieres cambiar de contraseña contacte al administrador'
                msg.attach(MIMEText(mensaje, 'plain'))

                # Establecer conexión con el servidor SMTP
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)

                # Enviar el correo electrónico
                server.sendmail(sender_email, correo, msg.as_string())

                # Cerrar la conexión
                server.quit()
                return Response(status= status.HTTP_200_OK) 
        return Response(status=status.HTTP_400_BAD_REQUEST)