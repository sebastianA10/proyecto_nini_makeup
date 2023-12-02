from rest_framework import routers
from .api import ProductosRegistroViewsSet

router = routers.DefaultRouter()
router.register('api/app1', ProductosRegistroViewsSet, 'app1')
urlpatterns = router.urls