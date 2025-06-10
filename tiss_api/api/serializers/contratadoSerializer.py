from tiss_api.models import Contratado
from rest_framework import serializers

class ContratadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contratado
        fields = ['nome_contratado', 'cnes', 'codigo_operadora']

    # Validaçções dos campos referentes a tamanho, típos e valores.
    def validate_cnes(self, value):
        if not value.isdigit() or len(value) != 7:
            raise serializers.ValidationError("O CNES deve ter exatamente 7 dígitos numéricos")
        return value
    
    def validate_codigo_operadora(self, value):
        if not value.isdigit() or len(value) != 14:
            raise serializers.ValidationError("O código da operadora deve conter até 14 dígitos numéricos")
        return value
    
    def validate_nome_contratado(self, value):
        if not value or len(value) > 70:
            raise serializers.ValidationError("O nome do contratado deve ter até 70 caracteres")
        return value