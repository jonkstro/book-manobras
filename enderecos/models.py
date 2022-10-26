from django.db import models


class Enderecos(models.Model):
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=25)
    estado = models.CharField(max_length=25)
    pais = models.CharField(max_length=25)
    latitude = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=10)
    lontitude = models.DecimalField(blank=True, null=True, max_digits=15, decimal_places=10)

    def __str__(self):
        return self.bairro