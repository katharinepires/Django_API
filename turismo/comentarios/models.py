from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentarios = models.TextField(default="")
    data = models.DateTimeField(auto_now_add=True)
    relevante = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username