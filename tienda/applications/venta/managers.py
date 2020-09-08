from django.db import models

class SaleDetailManager(models.Manager):
    
    # Listar producto de una venta
    def producto_por_venta(self, id_venta ):

        return self.filter(
            sale__id=id_venta
        ).order_by('count', 'product__name')