from django.db import models


class Acoes(models.Model):
    class Meta:
        db_table = 'acoes'

    empresa = models.CharField(max_length=200)
    codigo = models.CharField(max_length=200)
    ultimo_fechamento = models.CharField(max_length=200)
    maxima52semanas = models.CharField(max_length=200)
    minima52semanas = models.CharField(max_length=200)
    qtdnegociado_21dias = models.CharField(max_length=200)
    volume_medio = models.CharField(max_length=200)
    data_json = models.CharField(max_length=200)

    def __str__(self):
        return self.empresa