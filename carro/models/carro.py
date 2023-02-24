from django.db import models
from carro.models.marca import Marca


class Carro(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.DO_NOTHING)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.CharField(max_length=100)
    placa = models.CharField(max_length=8)
    categoria = models.CharField(max_length=1)
    preco_diaria = models.IntegerField()

    def __str__(self):
        return self.nome
