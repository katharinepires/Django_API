from django.db import models

# Create your models here.
class Atividades(models.Model):
    nome = models.CharField(max_length=100, default="")
    descricao = models.TextField(default="")
    horario_funcionamento = models.TextField(default="")
    idade = models.IntegerField(default="")
    foto = models.ImageField(upload_to='atividades', null=True, blank=True)

    def __str__(self):
        return self.nome