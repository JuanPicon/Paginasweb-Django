from django.db import models

# Create your models here.
class Estanterías(models.Model):
    Nombre = models.CharField(max_length=60)
    Precio = models.FloatField()
    Días_de_entrega = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Lockers(models.Model):
    Nombre = models.CharField(max_length=60)
    Precio = models.FloatField()
    Días_de_entrega = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Muebles_de_oficina(models.Model):
    Nombre = models.CharField(max_length=60)
    Precio = models.FloatField()
    Días_de_entrega = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre

class Cajas_plásticas(models.Model):
    Nombre = models.CharField(max_length=60)
    Precio = models.FloatField()
    Días_de_entrega = models.CharField(max_length=60)

    def __str__(self):
        return self.Nombre
