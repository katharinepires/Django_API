from rest_framework.viewsets import ModelViewSet
from atividades.models import Atividades
from .serializers import AtividadesSerializer

class AtividadesViewSet(ModelViewSet):
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer
    filter_fields = ('nome', 'descricao')