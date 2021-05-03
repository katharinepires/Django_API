from django.db import models

# Create your models here.
class Localizacao(models.Model):
    endereco = models.CharField(max_length=100)
    numero = models.IntegerField(null=True, blank=True)
    bairro = models.CharField(max_length=100)
    ponto_referencia = models.CharField(max_length=100,  null=True, blank=True)

    def __str__(self):
        return self.endereco