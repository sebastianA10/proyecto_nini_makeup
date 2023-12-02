from .models import ProductosRegistro
from rest_framework import viewsets, permissions
from .serializers import ProductosRegistroSerializer

class ProductosRegistroViewsSet(viewsets.ModelViewSet):
    queryset = ProductosRegistro.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductosRegistroSerializer  # Corregido el nombre de la propiedad
