from django.db import models


class Local(models.Model):
    nome = models.CharField(max_length=150)
    cep = models.IntegerField()

    def __str__(self):
        return self.nome
