from rest_framework import serializers
from models import Paciente
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id','nome','rg','cpf','data_nascimento']