from rest_framework.serializers import ModelSerializer
from atividades.models import Atividades

class AtividadesSerializer(ModelSerializer):
    class Meta:
        model = Atividades
        fields = ('nome', 'descricao', 'horario_funcionamento', 'idade', 'foto')