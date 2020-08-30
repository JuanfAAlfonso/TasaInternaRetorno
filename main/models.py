from django.db import models


class Indicadores(models.Model):
    fondo = models.IntegerField()
    fecha = models.DateField(unique=True)
    Valor = models.DecimalField(decimal_places=6, max_digits=100000000)

    def __str__(self):
        return self.fondo+' '+self.fecha+' '+self.valor


class Dividendos(models.Model):
    fondo = models.IntegerField()
    fecha = models.DateField()
    valor = models.DecimalField(decimal_places=6, max_digits=100000000)

    def __str__(self):
        return self.fondo+' '+self.fecha+' '+self.valor