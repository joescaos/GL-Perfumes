from django.db import models

class Perfume(models.Model):
    nombre = models.CharField(max_length=80)
    referencia = models.CharField(max_length=80)
    imagen = models.ImageField(upload_to='perfume/', null=True)
    precio = models.PositiveIntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Perfume'
        verbose_name_plural = 'Perfumes'
