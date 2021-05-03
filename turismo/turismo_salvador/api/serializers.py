from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from turismo_salvador.models import TurismoSalvador
from atividades.api.serializers import AtividadesSerializer
from localizacao.api.serializers import LocalizacaoSerializer
from avaliacoes.api.serializers import AvaliacoesSerializer

class TurismoSalvadorSerializer(ModelSerializer):
    atividades = AtividadesSerializer(many=True)
    localizacao = LocalizacaoSerializer()
    avaliacoes = AvaliacoesSerializer(many=True)
    desc_completa = SerializerMethodField()


    class Meta:
        model = TurismoSalvador
        fields = ['id', 'nome', 'descricao', 'recomendado', 'foto','atividades', 'localizacao', 'avaliacoes', 'desc_completa', 'desc_completa2']
        #read_only_fields = ['comentarios', 'avaliacoes']

    
    def get_desc_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)