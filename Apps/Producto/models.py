from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    oferta = models.BooleanField()

    def __str__(self):
        return 'Nombre: {}, Precio: {}, Oferta: {}'.format(self.nombre, self.precio, self.oferta)
    