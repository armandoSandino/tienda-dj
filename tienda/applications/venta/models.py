from django.db import models
from django.conf import settings

#
from model_utils.models import TimeStampedModel

# local apps
from applications.producto.models import Product


class Sale(TimeStampedModel):
    """Modelo que representa a una Venta Global"""

    TIPO_INVOCE = (
        ('0', 'BOLETA'),
        ('3', 'FACTURA'),
        ('4', 'OTRO'),
    )

    TIPO_PAYMENT = (
        ('0', 'TARJETA'),
        ('1', 'DEPOSITO'),
        ('2', 'CONTRAENTREGA'),
    )

    FLAT_STATE = (
        ('0', 'En Proceso'),
        ('1', 'En Envio'),
        ('2', 'En Tienda'),
        ('3', 'Entregado'),
    )

    date_sale = models.DateTimeField(
        'Fecha de Venta',
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        'Monto', 
        max_digits=10, 
        decimal_places=2
    )
    count = models.PositiveIntegerField('Cantidad de Productos')
    type_invoce = models.CharField(
        'TIPO',
        max_length=2,
        choices=TIPO_INVOCE
    )
    cancelado = models.BooleanField(default=False)
    type_payment = models.CharField(
        'TIPO PAGO',
        max_length=2,
        choices=TIPO_PAYMENT
    )
    state = models.CharField(
        'Estado de Envio',
        max_length=2,
        choices=FLAT_STATE,
        blank=True
    )
    adreese_send = models.TextField(
        'Direccion de Envio',
        blank=True,
    )
    anulate = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="usuario_venta",
        #editable=False
    )

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'ventas'

    def __str__(self):
        return 'Nº [' + str(self.id) + '] - ' + str(self.date_sale)



class SaleDetail(TimeStampedModel):
    """Modelo que representa a una venta en detalle"""

    sale = models.ForeignKey(
        Sale, 
        on_delete=models.CASCADE, 
        verbose_name='Codigo de Venta'
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField('Cantidad')
    price_purchase = models.DecimalField(
        'Precio Compra', 
        max_digits=10, 
        decimal_places=3
    )
    price_sale = models.DecimalField(
        'Precio Venta', 
        max_digits=10, 
        decimal_places=2
    )
    anulate = models.BooleanField(default=False)
    #

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de una Venta'

    def __str__(self):
        return str(self.sale.id) + ' - ' + str(self.product.name)
