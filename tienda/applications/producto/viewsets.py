from rest_framework import viewsets
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