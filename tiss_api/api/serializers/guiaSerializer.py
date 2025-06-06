from rest_framework.serializers import ModelSerializer
from tiss_api.models.Guias import *

class GuiaConsultaSerializer(ModelSerializer):
    class Meta:
        model = GuiaConsulta
        fields = '__all__'