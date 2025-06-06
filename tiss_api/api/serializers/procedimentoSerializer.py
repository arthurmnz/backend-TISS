from rest_framework.serializers import ModelSerializer
from tiss_api.models.Procedimento import Procedimento 

class ProcedimentoSerializer(ModelSerializer):
    class Meta:
        model = Procedimento
        fields = '__all__'