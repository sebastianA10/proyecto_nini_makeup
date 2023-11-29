from .models import Productos
from rest_framework import viewsets,permissions

class productosviewsets (viewsets.ModelViewSet):

 queryset=Productos.objects.all()
permission_classes= [permissions.AllwAny]