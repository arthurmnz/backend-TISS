from rest_framework.serializers import ModelSerializer
from tiss_api.models import Procedimento

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = ['tabela', 'codigo_procedimento', 'descricao']

        def validate_tabela(self, value):
            if value not in dict(Procedimento.TABELA_PROCEDIMENTOS_CHOICES).keys():
                raise ModelSerializer.ValidationError("Tabela inválida. Escolha uma valor válido na tabela")
            return value
        
        def validate_codigo_procedimento(self, value):
            if value is None or len(value) > 10:
                raise ModelSerializer.ValidationError("O código de procedimento deve conter até 10 caracteres")
            return value
        
        def validate_descricao(self, value):
            return value
