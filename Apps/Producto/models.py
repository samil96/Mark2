from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    oferta = models.BooleanField()

    def __str__(self):
        return 'Nombre: {}, Precio: {}, Oferta: {}'.format(self.nombre, self.precio, self.oferta)
"""
class tag(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{} | {}'.format(self.producto.nombre , self.nombre)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'producto']

    def __str__(self):
        return '{}'.format(self.producto)


"""