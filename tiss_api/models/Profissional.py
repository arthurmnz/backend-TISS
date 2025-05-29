from django.db import models

class Profissional(models.Model):  # Campos 12, 13, 14, 15, 16
    nome_profissional = models.CharField(max_length=255)  # 12
    conselho_profissional = models.CharField(max_length=100)  # 13
    numero_conselho_profissional = models.CharField(max_length=50)  # 14
    uf_profissional = models.CharField(max_length=2)  # 15
    cbo_profissional = models.CharField(max_length=10)  # 16
