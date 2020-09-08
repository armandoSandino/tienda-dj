# 
from rest_framework.generics import (
    ListAPIView
)
from django.shortcuts import render
# serializers
from .serializers import ProductSerializer
# models
from .models import Product


class ListProductUser(ListAPIView):

    # definir el serializador
    serializer_class = ProductSerializer

    def get_queryset(self):

        return Product.objects.all()