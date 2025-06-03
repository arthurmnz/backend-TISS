from django.db import models

# Campos 4, 5, 6, 7, 26 (Páginas 15 e 16 no pdfj)
class Beneficiario(models.Model):
    numero_carteira = models.CharField(max_length=4, blank=False, null=False) # 4
    validade_carteira = models.DateField(blank=True, null=False) # 5
    atendimento_rn = models.BooleanField(blank=False, null=False)  # 6
    nome = models.CharField(max_length=70, blank= False, null=False) # 7
    nome_social = models.CharField(max_length=70, blank=True, null=False)  # 26

    def __str__(self):
        return self.nome
