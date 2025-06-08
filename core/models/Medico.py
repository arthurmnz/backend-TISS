from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=70, blank = False, null = False)
    crm = models.CharField(max_length=15, unique =True, blank = False, null= False) 
    especialidade = models.CharField(max_length=50, blank = False, null= False)
    email = models.EmailField(unique=True, blank = False, null = False)
    telefone = models.CharField(max_length=11, blank= False, null = False)
    data_contratacao = models.DateField(blank = False, null = False)
    ativo = models.BooleanField(default=True)  #Se ainda trabalha na clínica. 

    def __str__(self):
        return f"Dr(a). {self.nome} - {self.especialidade}"
