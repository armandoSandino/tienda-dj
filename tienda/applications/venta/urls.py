from django.urls import path, re_path, include
# views
from .views import (
    ReporteVentasListAPIView,
    RegistrarVentaCreateAPIView,
    RegistrarVentaCreateAPIView2,
)

app_name = 'venta_app'

urlpatterns = [
    # ListAPIView
    path(
        'api/venta/reporte/',
        ReporteVentasListAPIView.as_view(),
        name='list'
    ),
    # CreateAPIView
    path(
        'api/venta/agregar/',
        RegistrarVentaCreateAPIView.as_view(),
        name='add-sale'
    ),
    # CreateAPIView
    path(
        'api/venta/add/',
        RegistrarVentaCreateAPIView2.as_view(),
        name='add-sale2'
    )
]