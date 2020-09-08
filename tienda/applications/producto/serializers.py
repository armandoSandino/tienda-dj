from  rest_framework import serializers
# models
from .models import Product, Colors

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colors
        fields = (
            'color',
        )

class ProductSerializer(serializers.ModelSerializer):

    # especificar que muestre el contenido de una llave foranea con ralacion de muchos a muchos
    #  en sustitucion de su identificador
    colors = ColorSerializer(many=True)

    class Meta:
        
        model = Product
        fields = (
            'name',
            'description',
            'man',
            'woman',
            'weight',
            'price_purchase',
            'price_sale',
            'main_image',
            'image1',
            'image2',
            'image3',
            'image4',
            'colors',
            'video',
            'stok',
            'num_sales',
            'user_created',
        )
