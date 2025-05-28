from django.db import models

class Contratado(models.Model):
    codigo_operadora = models.CharField(max_length=14)
    nome_contratado = models.CharField(max_length=70) 
    cnes = models.CharField(max_length=7) 

    def __str__(self):
        return self.nome_contratado

class Beneficiario(models.Model):
    nome = models.CharField(max_length=70) 
    nome_social = models.CharField(max_length=70, blank=True, null=True) 
    numero_carteira = models.CharField(max_length=20) 
    validade_carteira = models.DateField(blank=True, null=True) 
    atendimento_rn = models.BooleanField() 
    
    def __str__(self):
        return self.nome

class profissional(models.Model):
    nome_profissional = models.CharField(max_length=70) ##
    conselho_profissional = models.CharField(max_length=2) ##
    numero_conselho_profissional = models.CharField(max_length=15) ##
    uf_profissional = models.CharField(max_length=2) ##
    cbo_profissional = models.CharField(max_length=6) ##
    
    def __str__(self):
        return self.nome_profissional

class Procedimento(models.Model):
    tabela = models ##
    codigo_procedimento = models ##
    descricao_procedimento = models ##
    quantidade_solicitada = models ##
    quantidade_autorizada = models ##

class GuiaBase(models.Model):
    registro_ans = models.CharField(max_length=6) 
    numero_guia = models.CharField(max_length=20, unique=True) 
    tipo_guia = models.CharField(max_length=2, choices=[
        ('01', 'Consulta'),
        ('02', 'SPSADT'),
        ('03', 'Internação'),
    ])
    
    class Meta:
        abstract = True
        
class GuiaConsulta(GuiaBase):
    #dados gerais
    #no anymore
     
    #dados do beneficiário
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE) 

    #dados do contradado
    contratado = models.ForeignKey(Contratado, on_delete=models.CASCADE) 
    
    #dados do profissional
    profissional = models.ForeignKey(profissional, on_delete=models.CASCADE, related_name="profissional", blank=True, null=True)
    
    #dados do atendimento / procedimento
    indicacao_acidente = models ##
    indicador_cobertura_especial = models
    regime_atendimento = models
    saude_ocupacional = models ##
    data_atendimento = models.DateField()
    tipo_consulta = models.CharField(max_length=1, choices=[
        ('1', 'Primeira Consulta'),
        ('2', 'Retorno'),
        ('3', 'Consulta de Revisão'),
        ('4', 'Consulta de Alta'),
        ('5', 'Consulta de Emergência'),
        ('6', 'Consulta de Urgência'),
        ('7', 'Consulta de Pré-Natal'),
        ('8', 'Consulta de Pós-Parto'),
        ('9', 'Outros'),], default='1') ##
    tabela = models.CharField(max_length=2) 
    codigo_procedimento = models.CharField(max_length=10) 
    valor_procedimento = models.DecimalField(max_digits=8, decimal_places=2) 
    observacao = models.TextField(blank=True, null=True) 

class GuiaSPSADT(GuiaBase):
    #dados gerais    
    data_autorizacao = models.DateField(blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    data_validacao_senha = models.DateField(blank=True, null=True)
    numero_guia_principal = models.CharField(max_length=20, blank=True, null=True)
    
    #dados do beneficiário
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    
    #dados do solicitate
    contratado_solicitante = models.ForeignKey(Contratado, on_delete=models.CASCADE) 
    
    #profissional solicitante
    profissional_solicitante = models.ForeignKey(profissional, on_delete=models.CASCADE, related_name="profissional_solicitante", blank=True, null=True) 
    
    #Dados da Solicitação / Procedimentos ou Itens Assistenciais Solicitados
    carater_atendimento = models
    data_solicitacao = models.DateField()
    indicacao_clinica = models
    indicador_cobertura_especial = models
    #lista até 5 items
    procedimentos = models.ManyToManyField(Procedimento, blank=True, related_name="procedimentos_internacao")
    
    #Dados do Contratado Executante
    contratado_executante = models.ForeignKey(Contratado, on_delete=models.CASCADE)
    
    #dados do atendimento 
    indicacao_acidente = models ##
    tipo_consulta = models.CharField(max_length=1, choices=[
        ('1', 'Primeira Consulta'),
        ('2', 'Retorno'),
        ('3', 'Consulta de Revisão'),
        ('4', 'Consulta de Alta'),
        ('5', 'Consulta de Emergência'),
        ('6', 'Consulta de Urgência'),
        ('7', 'Consulta de Pré-Natal'),
        ('8', 'Consulta de Pós-Parto'),
        ('9', 'Outros'),], default='1') ##
    saude_ocupacional = models ##
    
    #Dados da Execução / Procedimentos e Exames Realizados
    #lista até 5 items
    data = models
    hora_inicial = models
    hora_final = models
    tabela = models 
    codigo = models 
    descricao = models 
    quantidade = models 
    via_acesso = models 
    tecnica = models 
    fator_reducao = models 
    valor_unitario = models 
    valor_total = models 
    
    #Identificação do(s) Profissional(is) Executante(s)
    sequencial_procedimento = models
    grau_participacao = models
    codigo_operadora = models
    profissional_executante = models    

class GuiaInternacao(GuiaBase):
    #dados gerais
    data_autorizacao = models.DateField(blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)
    data_validacao_senha = models.DateField(blank=True, null=True)

    #dados do beneficiário
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    
    #dados do contratado solicitante
    contratado_solicitante = models.ForeignKey(Contratado, on_delete=models.CASCADE, related_name="contratado_solicitante", blank=True, null=True)
    
    #profissional solicitante
    profissional_solicitante = models.ForeignKey(profissional, on_delete=models.CASCADE, related_name="profissional_solicitante_internacao", blank=True, null=True)
    
    #dadps da internação
    
    # procedimentos
    #listas até 12 items
    procedimentos = models.ManyToManyField(Procedimento, blank=True, related_name="procedimentos_internacao")
    
    #dados da autorização    
    
class lote(models.Model):
    numero_lote = models.CharField(max_length=20, unique=True) # 3
    data_envio = models.DateField() # 6
    status = models.CharField(max_length=20, choices=[
        ('PENDENTE', 'Pendente'),
        ('ENVIADO', 'Enviado'),
        ('PROCESSADO', 'Processado'),
        ('ERRO', 'Erro')
    ], default='PENDENTE') # 20
    observacao = models.TextField(blank=True, null=True) # 21
    guias = models.ManyToManyField(GuiaBase, blank=True, related_name="lotes")

