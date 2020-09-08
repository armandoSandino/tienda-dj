#models
from django.db import models

class ProductManager(models.Manager):

    def productos_por_usuario(self, el_usuario):

        return self.filter(
            user_created=el_usuario
        )