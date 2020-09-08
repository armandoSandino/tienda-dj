#
from django.utils import timezone
#
from django.shortcuts import render
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
# generic views
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
# models
from applications.producto.models import Product
from .models import Sale, SaleDetail
# serializers
from .serializers import (
    SaleSerializers,
    ProcesoVentaSerializers
)

class ReporteVentasListAPIView(ListAPIView):

    # definir el serializador
    serializer_class = SaleSerializers

    def get_queryset(self):
        return Sale.objects.all()


class RegistrarVentaCreateAPIView(CreateAPIView):
    ''' crear venta '''

    # definir serializador 
    serializer_class =  ProcesoVentaSerializers

    # definir el tipo de autenticacion para poder implementar este recurso
    # Decifrara el token e identificara/autenticara al usuario
    authentication_classes = (TokenAuthentication,)

    # Definir los tipos de permisos tiene habilitados esta vista
    permission_classes = [IsAuthenticated ] # IsAdminUser, IsAuthenticated

        # sobreescribir la function 'create'
    def create(self, request, *args, **kwargs):
        # deserializar los datos enviados desde el request
        # datos_serializados =  ProductoDetailSerializers(data=request.data)
        datos_serializados =  self.get_serializer(data=request.data)
        # validar que el los datos serializados sean correctos
        datos_serializados.is_valid(raise_exception=True)
        # si los datos son correctos podemos obtenerlos
        tipo_recibo = datos_serializados.validated_data['type_invoce']
        # crear la venta
        la_venta = Sale.objects.create(
            date_sale= timezone.now(),
            amount= 0,
            count= 0,
            type_invoce=  datos_serializados.validated_data['type_invoce'],
            type_payment=  datos_serializados.validated_data['type_payment'],
            adreese_send= datos_serializados.validated_data['adreese_send'],

            user= self.request.user ,
        )
        
        # calcular monto total de l venta
        monto = 0
        # calcular la cantidad de ejemplar por producto
        cantidad = 0

        # recuperar productos de la venta
        productos  =  datos_serializados.validated_data['productos']
        #
        ventas_detalle = []
        for item in productos:
            # el 'pk' y el 'count' esta definido en el realizador ProductoDetailSerializers
            # Obtener el producto por su ID
            prod = Product.objects.get(id=item['pk'])
            # crear del detalle de la venta
            detalle = SaleDetail(
                sale=la_venta,
                product=prod,
                count=item['count'],
                price_purchase= prod.price_purchase,
                price_sale= prod.price_sale
            )
            # calcular monto
            monto = monto + prod.price_sale * item['count']
            # calcular cantidad total
            cantidad = cantidad + item['count']

            # agregar producto al detalle
            ventas_detalle.append(detalle)

        # actualizar monto y cantidad de la venta
        la_venta.amount = monto
        la_venta.count = cantidad
        la_venta.save()

        # bulk_create, realiza una multiple insercion de registros a partir de un arreglo de datos
        SaleDetail.objects.bulk_create(ventas_detalle)

        return Response({
            'response': True,
            'message': 'Success operations'
        })
        #self.perform_create(serializer)
        #headers = self.get_success_headers(serializer.data)
        #return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
