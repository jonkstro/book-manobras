from django.db import models


class Manobras(models.Model):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    # procedimentos

    def __str__(self):
        return self.descricao