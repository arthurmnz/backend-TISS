from django.db import models

class Prestador(models.Model):
    codigo_operadora = models.CharField(max_length=14) # 13
    nome_contratado = models.CharField(max_length=70) # 14
    cnes = models.CharField(max_length=7) # 31
    
    def __str__(self):
        return self.nome_contratado

class Procedimento(models.Model):
    guia_consulta = models.ForeignKey("GuiaConsulta", on_delete=models.CASCADE, null=True, blank=True, related_name="procedimentos_consulta")
    guia_spsadt = models.ForeignKey("GuiaSPSADT", on_delete=models.CASCADE, null=True, blank=True, related_name="procedimentos_spsadt")
    
    data = models.DateField(blank=True, null=True) # 36 # 22
    hora_inicial = models.TimeField(blank=True, null=True) # 37 
    hora_final = models.TimeField(blank=True, null=True) # 38

    tabela = models.CharField(max_length=2) # 24 # 39
    codigo = models.CharField(max_length=10) # 25 # 40
    descricao = models.CharField(max_length=150) # 26 # 41
    quantidade = models.IntegerField() #27 # 42
    
    via_acesso = models.CharField(max_length=1, blank=True, null=True) # 43
    tecnica = models.CharField(max_length=1, blank=True, null=True) # 44
    fator_reducao = models.DecimalField(max_digits=4, decimal_places=2, default=1.00) # 45 
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2) # 46
    valor_total = models.DecimalField(max_digits=10, decimal_places=2) # 47

    observacao = models.TextField(blank=True, null=True)

class Paciente(models.Model):
    nome = models.CharField(max_length=70) # 10
    nome_social = models.CharField(max_length=70, blank=True, null=True) # 89
    numero_carteira = models.CharField(max_length=20) #8
    validade_carteira = models.DateField(blank=True, null=True) # 9
    atendimento_rn = models.BooleanField() # 12
    indicacao_acidente = models.CharField(max_length=1)  # 33
    
    def __str__(self):
        return self.nome

class GuiaBase(models.Model):
    registro_ans = models.CharField(max_length=6) # 1
    numero_guia_prestador = models.CharField(max_length=20, unique=True) # 2
    numero_guia_operadora = models.CharField(max_length=20, blank=True, null=True) # 7
    data_autorizacao = models.DateField(blank=True, null=True) # 4
    senha_autorizacao = models.CharField(max_length=20, blank=True, null=True) # 5

    class Meta:
        abstract = True
        
class GuiaConsulta(GuiaBase):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    nome_profissional = models.CharField(max_length=70)
    conselho = models.CharField(max_length=2)
    numero_conselho = models.CharField(max_length=15)
    uf = models.CharField(max_length=2)
    cbo = models.CharField(max_length=6)
    data_atendimento = models.DateField()
    tipo_consulta = models.CharField(max_length=1)
    tabela = models.CharField(max_length=2)
    codigo_procedimento = models.CharField(max_length=10)
    valor_procedimento = models.DecimalField(max_digits=8, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)

class GuiaSPSADT(GuiaBase):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    profissional_solicitante = models.CharField(max_length=70) # 15
    conselho_solicitante = models.CharField(max_length=2) # 16
    numero_conselho_solicitante = models.CharField(max_length=15) # 17
    uf_solicitante = models.CharField(max_length=2) # 18
    cbo_solicitante = models.CharField(max_length=6) # 19
    tipo_atendimento = models.CharField(max_length=2) # 32
    indicacao_clinica = models.TextField(blank=True, null=True) # 23
    tipo_consulta = models.CharField(max_length=1, blank=True, null=True) # 34
    motivo_encerramento = models.CharField(max_length=2, blank=True, null=True) # 35
    procedimentos = models.ManyToManyField(Procedimento, blank=True, related_name="guias_spsadt")
    total_geral = models.DecimalField(max_digits=10, decimal_places=2)



