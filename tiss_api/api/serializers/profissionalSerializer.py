from rest_framework.serializers import ModelSerializer
from tiss_api.models.Profissional import Profissional

class ProfissionalSerializer(ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'