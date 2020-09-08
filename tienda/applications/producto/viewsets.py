from rest_framework import viewsets
from rest_framework.response import Response
# models
from .models import Colors, Product
# serializers
from .serializers import (
    ColorSerializer,
    ProductSerializer,
    PaginationSerialize,
    ProductSerializerViewSet
)

# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#Debido a que se ModelViewSetextiende GenericAPIView, normalmente necesitará proporcionar al menos los atributos querysety serializer_class
class ColorViewSet(viewsets.ModelViewSet):
    

    # obligatorio definir el queryset
    queryset = Colors.objects.all()

    # Obligatorio definir el serializador
    serializer_class = ColorSerializer
    #

class ProductViewSet(viewsets.ModelViewSet):

    # obligatorio definir el queryset
    queryset = Product.objects.productos_con_stock()
    
    # Obligatorio definir el serializador
    serializer_class = ProductSerializerViewSet
    
    #agregar paginacion
    pagination_class = PaginationSerialize

    # https://www.django-rest-framework.org/api-guide/viewsets/#viewset-actions
    '''
    def create(self, request):
        
        print(request.data)
        
        return Response({
            'response': True,
            'message': 'Success operations'
        })
    '''

    # http://www.cdrf.co/3.1/rest_framework.viewsets/ModelViewSet.html#perform_create
    # El perform_create se llama a agregar un registro, puedes interctarlo para realizar los cambios que necesites antes de guardar
    def perform_create(self, serializer):
        serializer.save(
            video="http://www.cdrf.co/3.1/rest_framework.viewsets/ModelViewSet.html#perform_create"
        )

    # http://www.cdrf.co/3.1/rest_framework.viewsets/ModelViewSet.html#list 
    # list, le permitira cambiar la forma en la que se listan los registros   
    def list(self, request, *args, **kwargs):
        
        # mostrar productos por usuario
        queryset = Product.objects.productos_por_usuario( self.request.user )

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
