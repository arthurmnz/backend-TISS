from django.db import models


class Paciente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefere não informar'),
    ]

    clinica = models.ForeignKey(
        'Clinica', on_delete=models.CASCADE, related_name='pacientes')
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.TextField(blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"
