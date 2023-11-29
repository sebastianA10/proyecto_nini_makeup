from django.contrib import admin
from django.urls import path, include
from proyecto.views import Vistaproductos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('app1.urls')),
    path('productos/', Vistaproductos.as_view(), name='productos_list')
]
