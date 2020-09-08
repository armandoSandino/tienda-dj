from rest_framework import viewsets
# models
from .models import Colors
# serializers
from .serializers import ColorSerializer

# https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#Debido a que se ModelViewSetextiende GenericAPIView, normalmente necesitará proporcionar al menos los atributos querysety serializer_class
class ColorViewSet(viewsets.ModelViewSet):
    

    # obligatorio definir el queryset
    queryset = Colors.objects.all()

    # Obligatorio definir el serializador
    serializer_class = ColorSerializer
    #