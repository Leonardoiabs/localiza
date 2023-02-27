from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name='usuario')
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=400)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.user
