from rest_framework import routers
from .api import productosViewsSet

router = routers.DefaultRouter()
router.register('api/app1', productosViewsSet, 'app1')
urlpatterns = router.urls