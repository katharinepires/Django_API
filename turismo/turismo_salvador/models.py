from django.db import models
from atividades.models import Atividades
from comentarios.models import Comentarios
from avaliacoes.models import Avaliacoes
from localizacao.models import Localizacao

# Create your models here.
class TurismoSalvador(models.Model):
    nome = models.CharField(max_length=100, default="")
    descricao = models.TextField(default="")
    recomendado = models.BooleanField(default=False)
    atividades = models.ManyToManyField(Atividades)
    comentarios = models.ManyToManyField(Comentarios)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE, null=True, blank=True)
    foto = models.ImageField(upload_to='turismo_salvador', null=True, blank=True)

    @property
    def desc_completa2(self):
        return '%s - %s' % (self.nome, self.descricao)


    def __str__(self):
        return self.nome