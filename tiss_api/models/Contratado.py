from django.db import models

class Contratado(models.Model):  # Campos 9, 10, 11
    codigo_operadora = models.CharField(max_length=50)  # 9
    nome_contratado = models.CharField(max_length=255)  # 10
    cnes = models.CharField(max_length=20)              # 11

    def __str__(self):
        return self.nome_contratado
