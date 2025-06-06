from django.db import models
from tiss_api.models.Beneficiario import *
from tiss_api.models.Procedimento import *
from tiss_api.models.Contratado import  * 
from tiss_api.models.Profissional import *

INDICACAO_ACIDENTES = [
    ('0', 'Não'),
    ('1', 'Sim - Acidente Relacionado ao Trabalho'),
    ('2', 'Sim - Outros Tipos de Acidente')
]

COBERTURA_ESPECIAL = [
    ('PG', 'Atendimento à Gestante em Plano Hospitalar'),
    ('PN', 'Pré-Natal em Plano Hospitalar'),
    ('PP', 'Pós-Parto em Plano Hospitalar'),
    ('CO', 'Atendimento Cirúrgico Ambulatorial Pré-Operatório (Plano Hospitalar)'),
    ('CP', 'Atendimento Cirúrgico Ambulatorial Pós-Operatório (Plano Hospitalar)'),
]

REGIME_ATENDIMENTO_CHOICES = [
    ('01', 'Ambulatorial'),                       
    ('02', 'Hospital Dia'),                    
    ('03', 'Internação Hospitalar'),              
    ('04', 'Atendimento Domiciliar'),             
    ('05', 'Urgência/Emergência'),
]

TIPO_CONSULTA = [
    ('1', 'Primeira consulta'),
    ('2', 'Consulta de revisão'),
    ('3', 'Atendimento de urgência'),
]


STATUS_GUIA_CHOICES = [
    ('1', 'Normal'),
    ('2', 'Cancelada'),
    ('3', 'Substituída'),
    ('4', 'Glosada'),
    ('5', 'liquidada')
]

TABELA_PROCEDIMENTOS_CHOICES = [
    ('00', 'Tabela Própria da operadora'),
    ('01', 'Terminologia Unificada da Saúde Suplementar – TUSS – Procedimentos e Eventos em Saúde'),
    ('02', 'Terminologia Unificada da Saúde Suplementar – TUSS – Materiais'),
    ('03', 'Terminologia Unificada da Saúde Suplementar – TUSS – Medicamentos'),
    ('20', 'Tabela de Procedimentos, Medicamentos e OPM do SUS'),
    ('22', 'TUSS'),
    ('98', 'Tabela Não Contemplada pela TISS'),
]

class GuiaBase(models.Model):
    registro_ans = models.CharField(max_length=6,blank=False, null=False)  # 1
    numero_guia_prestador = models.CharField(max_length=20,blank=False, null=False)  # 2
    numero_guia_operadora = models.CharField(max_length=20,null=True, blank=True,)  # 3

    #fora do padrão tiss/ isso é para gestão
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_GUIA_CHOICES, default='')

    class Meta:
        abstract = True

#MISSÃO PRINCIPAL
class GuiaConsulta(GuiaBase):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    contratado = models.ForeignKey(Contratado, on_delete=models.CASCADE)
    profissional_executante = models.ForeignKey(Profissional, on_delete=models.CASCADE)

    indicacao_acidente = models.CharField(max_length=1,choices=INDICACAO_ACIDENTES, blank=False, null=False)  # 17
    indicador_cobertura_especial = models.CharField(max_length=2,choices=COBERTURA_ESPECIAL, blank=True, null=True)  # 27 
    regime_atendimento = models.CharField(max_length=2,choices=REGIME_ATENDIMENTO_CHOICES, blank=True, null=True)  # 28 
    saude_ocupacional = models.BooleanField(default=False)  # 29 

    data_atendimento = models.DateField(blank=False, null=True)  # 18  
    tipo_consulta = models.CharField(max_length=1,choices=TIPO_CONSULTA, blank=False, null=False)  # 19 

    tabela = models.CharField(max_length=2, choices=TABELA_PROCEDIMENTOS_CHOICES, blank=False, null=False)# detalha isso aq #obrigatorio
    codigo_procedimento = models.CharField(max_length=10, blank=False, null=False)# detalha isso aq # obrigatorio
    valor_procedimento = models.DecimalField(max_digits=10,decimal_places=2,blank=False,null=False) # detalha isso aq #obrigatorio

    observacao = models.TextField(blank=True, null=True)  # 23

    def __str__(self):
        return f"GuiaConsulta #{self.numero_guia_prestador} - {self.beneficiario.nome} - {self.profissional_executante.nome}. {self.data_atendimento}"

#MISSÃO SECUNDARIA
# class GuiaSPSADT(GuiaBase):
#     numero_guia_principal = models.CharField(max_length=20, blank=True, null=True)  # 3
#     data_autorizacao = models.DateField(blank=True, null=True)  # 4
#     senha = models.CharField(max_length=50, blank=True, null=True)  # 5 #verificar tamanho
#     validade_senha = models.DateField(blank=True, null=True)  # 6


#     beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)  # Campos 8–12

#     # Solicitante - Campos 13–20   
#     contratado_solicitante = models.ForeignKey()
#     profissional_solicitante = models.ForeignKey()

#     # Solicitações - Campos 21–28
#     caracter_atendimento = models.CharField() # 21
#     data_solicitacao = models.DateField(blank=True, null=True) # 22
#     indicacao_clinica = models.TextField(blank=True, null=True)  # 23
#     indicador_cobertura_especial = models.CharField(max_length=2, blank=True, null=False)  # 90 #choices
#     # campos 21-28 agrupados por item

#     procedimentos_solicitados = models

#     # Contratado Executante - Campos 29–31
#     contratado_executante = models.ForeignKey(Contratado, on_delete=models.CASCADE, related_name='guias_spsadt', blank=True, null=True)  # 29 - 31

#     # Atendimento - Campos 32–35, 91, 92
#     tipo_atendimento = models.CharField(max_length=2, blank=False, null=False)  # 32
#     indicacao_acidente = models.CharField(max_length=1, blank=False, null=False)  # 33
#     tipo_consulta = models.CharField(max_length=1, blank=True, null=False)  # 34
#     motivo_encerramento = models.CharField(max_length=2, blank=True, null=False)  # 35
#     regime_atendimento = models.CharField(max_length=2, blank=False, null=False)  # 91
#     saude_ocupacional = models.CharField(max_length=2, blank=True, null=False)  # 92

#     # Execução - Campos 36–47 (lista de procedimentos realizados)
#     procedimentos_realizados = models.ManyToManyField(Procedimento, blank=True, related_name='guias_spsadt_procedimentos')  # 36 a 47

#     # Identificação Profissionais - Campos 48–56 CUIDADO COM ESSES CAMPOS (DEIXAR POR ULTIMO)
#     cpf_executor = models.CharField(max_length=11, blank=True, null=True)  # 48
#     nome_profissional_exec = models.CharField(max_length=100, blank=True, null=True)  # 51
#     conselho_profissional_exec = models.CharField(max_length=50, blank=True, null=True)  # 52
#     numero_conselho_exec = models.CharField(max_length=50, blank=True, null=True)  # 53
#     uf_profissional_exec = models.CharField(max_length=2, blank=True, null=True)  # 54
#     cbo_profissional_exec = models.CharField(max_length=10, blank=True, null=True)  # 55

#     data_realizacao_procedimentos = models # 56

#     observacao_justificativa = models.TextField(blank=True, null=True)  # 58

#     # Totais - Campos 59–65
#     total_procedimentos = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 59
#     total_taxes_alugueis = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 60
#     total_materiais = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 61
#     total_opme = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 62
#     total_medicamentos = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 63
#     total_gases_medicinais = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)  # 64
#     total_geral = models.DecimalField(max_digits=8, decimal_places=2, blank=False, null=False)  # 65

#     def __str__(self):
#         return f"GuiaSPSADT #{self.numero_guia}"
