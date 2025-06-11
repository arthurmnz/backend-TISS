from rest_framework import ModelSerializer
from tiss_api.models import Guias

class GuiaConsultaSerializer(ModelSerializer):
    class Meta:
        model = Guias
        fields = '__all__'