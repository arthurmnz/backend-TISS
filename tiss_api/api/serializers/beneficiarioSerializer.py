from rest_framework import serializers
from tiss_api.models import Beneficiario

class BeneficiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiario
        fields = ['numero_carteira', 'validade_carteira', 'atendimento_rn', 'nome', 'nome_social']

    def validate_numero_carteira(self, value):
        if not value or len(value) > 20:
            raise serializers.ValidationError("O número da carteira deve conter até 20 caracteres")
        return value
    
    def validate_nome(self, value):
        if not value or len(value) > 70:
            raise serializers.ValidationError("O nome do beneficiário deve conter até 70 caracteres")
        return value
        
    def validate_nome_social(self, value):
        if value or len(value) > 70:
            raise serializers.ValidationError("O nome social do beneficiário deve conter até 70 caracteres")
        return value
        