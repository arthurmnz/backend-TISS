from django.db import models
from django.core.exceptions import ValidationError
import re


def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)
    if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * (peso - i) for i in range(peso - 1))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    digito1 = calcular_digito(cpf, 10)
    digito2 = calcular_digito(cpf, 11)

    if int(cpf[9]) != digito1 or int(cpf[10]) != digito2:
        raise ValidationError("CPF inválido.")


class Clinica(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Medico(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    ESPECIALIDADES_CHOICES = [
        ('Cardiologia', 'Cardiologia'),
        ('Dermatologia', 'Dermatologia'),
        ('Ortopedia', 'Ortopedia'),
        ('Pediatria', 'Pediatria'),
        ('Clínico Geral', 'Clínico Geral'),
    ]

    telefone_validator = models.RegexValidator(
        regex=r'^\(\d{2}\)\s9\d{4}-\d{4}$',
        message="Telefone deve estar no formato (XX) 9XXXX-XXXX"
    )

    nome = models.CharField(max_length=70, blank=False, null=False)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=False, null=False)
    crm = models.CharField(max_length=15, unique=True, blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True, validators=[validar_cpf], blank=False, null=False)
    especialidade = models.CharField(max_length=30, choices=ESPECIALIDADES_CHOICES, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    telefone = models.CharField(max_length=15, validators=[telefone_validator], blank=False, null=False)
    data_contratacao = models.DateField(blank=False, null=False)
    ativo = models.BooleanField(default=True)
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE, related_name='medicos', blank=False, null=False)

    def __str__(self):
        return f"Dr(a). {self.nome} - {self.especialidade}"