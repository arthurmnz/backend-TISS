from django.db import models

class Profissional(models.Model):  # Campos 12, 13, 14, 15, 16
    nome_profissional = models.CharField(max_length=70, blank= True, null=False)  # 12
    conselho_profissional = models.CharField(max_length=2,blank=False, null=False)  # 13
    numero_conselho_profissional = models.CharField(max_length=15,blank=False, null=False)  # 14
    uf_profissional = models.CharField(max_length=2, blank=False, null=False)  # 15
    cbo_profissional = models.CharField(max_length=6, blank=False, null=False)  # 16
