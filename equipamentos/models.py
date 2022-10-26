from django.db import models
from manobras.models import Manobras
from obs_equipamentos.models import ObsEquipamentos

class Equipamentos(models.Model):
    codigo = models.CharField(max_length=20, null=False, blank=False)
    statusNaNf = models.BooleanField()
    foto = models.ImageField(upload_to='equipamentos', null=True, blank=True)
    classeTensao = models.DecimalField(max_digits=5, decimal_places=1)
    correnteNominal = models.IntegerField()
    fabricante = models.CharField(max_length=20, null=False, blank=False)
    numSerie = models.CharField(max_length=20, null=False, blank=False)
    dataFabricacao = models.DateField()
    manobras = models.ManyToManyField(Manobras)
    observacoes = models.ManyToManyField(ObsEquipamentos)

    def __str__(self):
        return self.codigo
