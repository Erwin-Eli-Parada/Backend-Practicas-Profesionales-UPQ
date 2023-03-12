from .models import Usuario
from rest_framework import viewSets, permissions
from serializers import UsuarioSerializer

class UsuarioViewSet(viewSets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer