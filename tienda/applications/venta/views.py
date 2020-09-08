from django.shortcuts import render
# generic views
from rest_framework.generics import (
    ListAPIView
)
# models
from .models import Sale
# serializers
from .serializers import SaleSerializers

class ReporteVentasListAPIView(ListAPIView):

    # definir el serializador
    serializer_class = SaleSerializers

    def get_queryset(self):
        return Sale.objects.all()
