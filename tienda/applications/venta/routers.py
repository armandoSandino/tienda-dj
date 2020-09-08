from rest_framework.routers import DefaultRouter
# views
from . import viewsets

router = DefaultRouter()

# agregar rutas
router.register(r'ventas', viewsets.ReporteVentasViewSet, basename='sales')

urlpatterns = router.urls
