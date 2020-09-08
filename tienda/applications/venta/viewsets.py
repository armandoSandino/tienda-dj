# generic viewsets
from rest_framework import viewsets
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response 
#
from django.shortcuts import get_object_or_404
from django.utils import timezone
#
from applications.producto.models import Product
# serializers
from .serializers import ProcesoVentaSerializers2, VentaReporteSerializers
# models
from .models import Sale, SaleDetail

#https://www.django-rest-framework.org/api-guide/viewsets/#viewsets
class ReporteVentasViewSet(viewsets.ViewSet):

    # definir el tipo de autenticacion para poder implementar este recurso
    # Decifrara el token e identificara/autenticara al usuario
    authentication_classes = (TokenAuthentication,)

    # Definir los tipos de permisos tiene habilitados esta vista
    #permission_classes = [IsAuthenticated ] # IsAdminUser, IsAuthenticated

    # definir serializador, no es obligatorio
    # serializer_class = VentaReporteSerializers

    # definir el queryset es obligatorio
    queryset = Sale.objects.all()

    # gestionar permisos para cada action de nuestro ViewSet
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if (self.action == 'list') or (self.action == 'retrieve'):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]


    # list, le permitira cambiar la forma en la que se listan los registros   
    def list(self, request, *args, **kwargs):
        
        queryset = Sale.objects.all()
        # si tocaria serializar muchos datos omitir el 2do parametro del serializador, many=True
        serializer = VentaReporteSerializers(queryset, many=True)
        return Response({
            'response': True,
            'message': 'Sucess operations',
            'data': serializer.data
        })

    # nos permite agregar registro
    def create(self, request):

        # deserializar los datos enviados desde el request
        datos_serializados =  ProcesoVentaSerializers2(data=request.data)
        #datos_serializados =  self.get_serializer(data=request.data)

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
        # id__in, buscara todos los id de la tabla producto con cada indice del arreglo 'productos' que viaja desde la url
        productos = Product.objects.filter(
            id__in=datos_serializados.validated_data['productos']
        )

        # recuperar cantidades
        cantidades = datos_serializados.validated_data['cantidades']

        #
        ventas_detalle = []
        for item, item_cantidad in zip(productos, cantidades):
            # crear del detalle de la venta
            detalle = SaleDetail(
                sale=la_venta,
                product=item,
                count=item_cantidad,
                price_purchase= item.price_purchase,
                price_sale= item.price_sale
            )

            # calcular monto
            monto = monto + item.price_sale * item_cantidad

            # calcular cantidad total
            cantidad = cantidad + item_cantidad

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
    

    # retrieve, es el equivalente al DetailView que nos recupera un determinado registro
    def retrieve(self, request, pk=None):
        
        # obtener la venta a mostrar
        #la_venta = Sale.objects.get(id=pk)
        queryset = Sale.objects.all()
        la_venta = get_object_or_404(queryset, id=pk)
        
        # serializar para responder
        serializer = VentaReporteSerializers(la_venta,)

        return Response({
            'response': True,
            'message': 'Success operation',
            'data': serializer.data
        })

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass