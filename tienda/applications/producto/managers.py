#models
from django.db import models

class ProductManager(models.Manager):

    def productos_por_usuario(self, el_usuario):

        return self.filter(
            user_created=el_usuario
        )
    
    def productos_con_stock(self):

        return self.filter(
            stok__gt=0,
        ).order_by('-num_sales')

    def productos_por_genero(self, genero ):

        if genero == 'm':
            mujer = True
            varon = False
        elif genero == 'v':
            varon = True
            mujer = False
        else: 
            varon = True
            mujer = True

        return self.filter(
            man=varon,
            woman=mujer
        ).order_by('created')