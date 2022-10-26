from django.db import models
from equipamentos.models import Equipamentos
from manobras.models import Manobras

from subestacoes.models import Subestacoes


class Servicos(models.Model):
    pt = models.IntegerField()
    subestacao = models.ForeignKey(Subestacoes, on_delete=models.DO_NOTHING)
    # equipamento = models.ForeignKey(Equipamentos, on_delete=models.DO_NOTHING)
    # manobra = models.ForeignKey(Manobras, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.pt