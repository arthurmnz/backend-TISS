from django.db import models

class Beneficiario(models.Model):  # Campos 4, 5, 6, 7, 26
    nome = models.CharField(max_length=255)              # 7
    nome_social = models.CharField(max_length=255, blank=True, null=True)  # 26
    numero_carteira = models.CharField(max_length=50)   # 4
    validade_carteira = models.DateField()  # 5
    atendimento_rn = models.BooleanField(default=False)  # 6

    def __str__(self):
        return self.nome
