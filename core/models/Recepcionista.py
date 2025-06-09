from django.db import models

class Recepcionista(models.Model):
    nome = models.CharField(max_length=70, blank = False, null = False)
    cpf = models.CharField(max_length=14, unique=True, blank = False, null = False)
    email = models.EmailField(unique=True, blank = False, null = False)
    telefone = models.CharField(max_length=11, blank= False, null = False)
    turno = models.CharField(
        max_length=10,
        choices=[('MANHA', 'Manhã'), ('TARDE', 'Tarde'), ('NOITE', 'Noite')],
        blank = True,
        null = False
    )
    data_admissao = models.DateField(blank = False, null= False)
    ativo = models.BooleanField(default=True, blank = False, null = False)

    def __str__(self):
        return self.nome
