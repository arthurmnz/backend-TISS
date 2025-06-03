from django.db import models

class Procedimento(models.Model):
    tabela = models.CharField(max_length=2, blank=True, null=False)  # 24
    codigo_procedimento = models.CharField(max_length=10, blank=False, null=False)  # 25
    
class ProcedimentosSolicitados(Procedimento):
    descricao = models.CharField(max_length=150, blank=False, null=False)  # 26
    quantidade_solicitado = models.PositiveIntegerField(blank=False, null= False)  # 27
    quantidade_autorizado = models.PositiveIntegerField(blank=False, null= False) # 28

#Campo 36 - 44 (Páginas 8 e 9 no pdf).
class ProcedimentoRealizado(Procedimento):
    data = models.DateField(blank=True, null=False) #36
    hora_inicio = models.TimeField(blank=True, null=False) #37
    hora_fim = models.TimeField(blank=True, null=False) #38
    descricao = models.CharField(max_length=150, blank=True, null=False) #41
    quantidade = models.PositiveIntegerField(blank=True, null=False) #42
    via_acesso = models.CharField(max_length=1, blank=True, null=False) #43
    tecnica = models.CharField(max_length=1, blank=True, null=False) #44
    valor_unitario = models.DecimalField(max_digits=6, decimal_places=2,blank=True, null=False) #46
    valor_total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=False) #47
