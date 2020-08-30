from django.db import models


class Dividendos(models.Model):
    fondo = models.IntegerField()
    fecha = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        db_table = 'Dividendos'


class Indicadores(models.Model):
    fondo = models.IntegerField()
    fecha = models.DateField(unique=True)
    valor = models.DecimalField(db_column='Valor', max_digits=10, decimal_places=5)  # Field name made lowercase. max_digits and decimal_places have been guessed, as this database handles decimal fields as float

    class Meta:
        db_table = 'Indicadores'
