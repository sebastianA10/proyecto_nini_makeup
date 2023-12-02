from .models import Productos
from rest_framework import viewsets, permissions
from .serializers import productosSerializer

class productosViewsSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = productosSerializer  # Corregido el nombre de la propiedad
