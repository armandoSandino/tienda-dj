#
from rest_framework.routers import DefaultRouter
# viewsets
from . import viewsets

router = DefaultRouter()

# agrega rutas
router.register(r'colors', viewsets.ColorViewSet , basename='colores')

urlpatterns = router.urls

