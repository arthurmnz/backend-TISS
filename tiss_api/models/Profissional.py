from django.db import models
from django.core.validators import RegexValidator

CONSELHO_CHOICES = [
    ('01', 'Conselho Regional de Medicina'),
    ('02', 'Conselho Regional de Odontologia'),
    ('06', 'Conselho Regional de Psicologia'),
]

UF_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
    ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'),
    ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'),
    ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
]

class Profissional(models.Model):  # Campos 12, 13, 14, 15, 16
    nome = models.CharField(max_length=70, blank= True, null=False)  # 12
    conselho_profissional = models.CharField(max_length=2,blank=False, choices=CONSELHO_CHOICES, null=False)  # 13
    numero_conselho = models.CharField(max_length=15,blank=False, null=False)  # 14
    uf = models.CharField(max_length=2, choices=UF_CHOICES, blank=False, null=False)  # 15
    codigo_cbo = models.CharField(max_length=6, blank=False, null=False)  # 16

    def __str__(self):
        return self.nome