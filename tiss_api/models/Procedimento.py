from django.db import models

class Procedimento(models.Model):
    tabela = models.CharField(max_length=50)  # 20
    codigo_procedimento = models.CharField(max_length=50)  # 21
    valor_procedimento = models.DecimalField(max_digits=10, decimal_places=2)  # 22
    
class ProcedimentosSolicitados(Procedimento):
    descricao = models.CharField(max_length=255)  # 26
    quantidade_solicitado = models.PositiveIntegerField()  # 27

class ProcedimentoRealizado(Procedimento):
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    descricao = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    via_acesso = models.CharField(max_length=100)
    tecnica = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
