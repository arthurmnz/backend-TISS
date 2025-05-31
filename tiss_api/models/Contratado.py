from django.db import models

class Contratado(models.Model):  # Campos 9, 10, 11
    codigo_operadora = models.CharField(max_length=14, blank=False, null=False)  # 9
    nome_contratado = models.CharField(max_length=70, blank=False, null=False)  # 10
    cnes = models.CharField(max_length=7, default='9999999',blank=False, null=False)              # 11

    def __str__(self):
        return self.nome_contratado
