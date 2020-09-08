#
from rest_framework.routers import DefaultRouter
# viewsets
from . import viewsets

router = DefaultRouter()

# agrega rutas
router.register(r'colors', viewsets.ColorViewSet , basename='colores')
router.register(r'products', viewsets.ProductViewSet, basename='productos')

urlpatterns = router.urls

