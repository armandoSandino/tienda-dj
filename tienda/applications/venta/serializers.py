#
from rest_framework import serializers
# models 
from .models import Sale, SaleDetail

class SaleDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        fields = (
            'id',

            'sale',

            'product',
            'count',
            'price_purchase',
            'price_sale',
        )

class SaleSerializers(serializers.ModelSerializer):
    # campo no definido en nuestro modelo
    # cojera su valor del resultado de una funcion get_producto mediante SerializerMethodField()
    producto = serializers.SerializerMethodField()

    class Meta:

        model = Sale

        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',

            'producto',
        )
    # obj, representara a cada registro sobre el que operar
    def get_producto(self, obj):
        
        consulta = SaleDetail.objects.producto_por_venta(obj.id)
        # Serializar el resultado de la consulta
        productos_serializados = SaleDetailSerializers(consulta,many=True ).data

        return productos_serializados


# serializers.Serializer, para serializar campos no relacionados a un modelo
class ProductoDetailSerializers(serializers.Serializer):

    pk = serializers.IntegerField()
    count = serializers.IntegerField()


# serializers.Serializer, para serializar campos no relacionados a un modelo
class ProcesoVentaSerializers(serializers.Serializer):

    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    #
    productos = ProductoDetailSerializers(many=True)








class ArrayIntergerSerializer( serializers.ListField ):

    child = serializers.IntegerField()

# serializers.Serializer, para serializar campos no relacionados a un modelo
# Un serializador que serialize un array
class ProcesoVentaSerializers2(serializers.Serializer):

    type_invoce = serializers.CharField()
    type_payment = serializers.CharField()
    adreese_send = serializers.CharField()
    #
    productos = ArrayIntergerSerializer()
    #
    cantidades = ArrayIntergerSerializer()

    # validar type_invoce, value es el valor actual de ese campo
    def validate_type_invoce(self, value ):
        if int(value) < 0 :
            raise serializers.ValidationError('ingrese un tipo de pago correcto...')

        return value

    # validar todos los campos, data contiene todos los campos
    def validate(self, data):

        if ( int(data['type_payment'])  < 0) or ( int(data['type_payment']) >= 3 ) :
            raise serializers.ValidationError('el metodo de pago no es correcto....')

        return data


class VentaReporteSerializers(serializers.ModelSerializer):
    # campo no definido en nuestro modelo
    # cojera su valor del resultado de una funcion get_producto mediante SerializerMethodField()
    producto = serializers.SerializerMethodField()

    class Meta:

        model = Sale

        fields = (
            'id',
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',

            'producto',
        )
    # obj, representara a cada registro sobre el que operar
    def get_producto(self, obj):
        
        consulta = SaleDetail.objects.producto_por_venta(obj.id)
        # Serializar el resultado de la consulta
        productos_serializados = SaleDetailSerializers(consulta,many=True ).data

        return productos_serializados