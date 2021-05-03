from rest_framework.serializers import ModelSerializer
from localizacao.models import Localizacao

class LocalizacaoSerializer(ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['endereco', 'numero', 'bairro', 'ponto_referencia']