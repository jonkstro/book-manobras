from django.db import models
from enderecos.models import Enderecos
from equipamentos.models import Equipamentos

class Subestacoes(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    codigo = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.ForeignKey(Enderecos, on_delete=models.CASCADE)
    regional = models.CharField(max_length=50, null=False, blank=False)
    equipamento = models.ManyToManyField(Equipamentos)

    def __str__(self):
        return self.codigo
