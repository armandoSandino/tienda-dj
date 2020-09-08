# 
from rest_framework.generics import (
    ListAPIView
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import render
# serializers
from .serializers import ProductSerializer
# models
from .models import Product


class ListProductUser(ListAPIView):

    # definir el serializador
    serializer_class = ProductSerializer
    # definir el tipo de autenticacion para poder implementar este recurso
    # Decifrara el token e identificara/autenticara al usuario
    authentication_classes = (TokenAuthentication,)

    # Definir los tipos de permisos tiene habilitados esta vista
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        # obtener usuario
        print(self.request.user)
        el_usuario = self.request.user

        return Product.objects.productos_por_usuario(el_usuario)