from typing_extensions import dataclass_transform
from rest_framework import serializers
from tiss_api.models.Profissional import Profissional

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ['nome', 'conselho_profissional', 'numero_conselho', 'uf', 'codigo_cbo']


    def validate_nome(self, value):
        if not value or len(value) > 70:
            raise serializers.ValidationError("O nome do contratado deve ter até 70 caracteres")
        return value

    def validate_conselho_profissional(self, value):
        if value not in dict(Profissional.CONSELHO_CHOICES).keys():
            raise serializers.ValidationError("Numero não válido para Conselho Regional")
        return value

    def validate_numero_conselho(self, value):
        if not value or len(value) > 15:
            raise serializers.ValidationError("Número de telefone inválido")
        return value

    def validate_uf(self, value):
        if value not in dict(Profissional.UF_CHOICES).keys():
            raise serializers.ValidationError("Estado registrado não existe")
        return value

    def validate_codigo_cbo(self, value):
        if value is None or len(value) > 6:
            raise serializers.ValidationError("Código CBO inválido")
