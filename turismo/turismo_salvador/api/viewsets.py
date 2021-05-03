from rest_framework.viewsets import ModelViewSet
from turismo_salvador.models import TurismoSalvador
from .serializers import TurismoSalvadorSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters

class TurismoSalvadorViewSet(ModelViewSet):
    #queryset = TurismoSalvador.objects.all()
    serializer_class = TurismoSalvadorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nome', 'descricao', 'localizacao__bairro']
    lookup_field = 'nome'  #não pode ter o nome repetido


#Filtrando o que aparecerá:
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = TurismoSalvador.objects.all()

        if id:
            queryset = TurismoSalvador.objects.filter(pk=id)
        
        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset
        #return TurismoSalvador.objects.filter(recomendado=False)

#Sobrescrever o método GET (lista que aparece):
    def list(self, request, *args, **kwargs):
        #return Response({'sobrescrevendo': 1999})
        return super(TurismoSalvadorViewSet, self).list(request, *args, **kwargs)

#Sobrescrever o método POST (aparecerá depois do criado):
    def create(self, request, *args, **kwargs):
        #return Response({'Olá': request.data['nome']})
        return super(TurismoSalvadorViewSet, self).create(request, *args, **kwargs)

#Sobrescrever o método DELETE (aparecerá depois de deltado):
    def destroy(self, request, *args, **kwargs):
        #return Response('Deletado com sucesso!')
        return super(TurismoSalvadorViewSet, self).destroy(request, *args, **kwargs)

#Actions personalizadas:
    @action(methods=['get', 'post'], detail=True)
    def denuncia(self, request, pk=None):
        pass
        #return super(TurismoSalvadorViewSet, self).create(request, *args, **kwargs)
        #return Response({'Olá': request.data['nome']})

    @action(methods=['get'], detail=False)
    def teste(self, request):
        #return super(TurismoSalvadorViewSet, self).create(request, *args, **kwargs)
        pass