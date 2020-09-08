#
from rest_framework import serializers
# models 
from .models import Sale, SaleDetail

class SaleDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        fields = ('__all__')

class SaleSerializers(serializers.ModelSerializer):

    class Meta:

        model = Sale

        fields = (
            'date_sale',
            'amount',
            'count',
            'type_invoce',
            'cancelado',
            'type_payment',
            'state',
            'adreese_send',
            'user',
        )

