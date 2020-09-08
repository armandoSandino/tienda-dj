from django.urls import path, re_path, include
# views
from .views import (
    ReporteVentasListAPIView
)

app_name = 'venta_app'

urlpatterns = [
    # ListAPIView
    path(
        'api/venta/reporte/',
        ReporteVentasListAPIView.as_view(),
        name='list'
    )
]