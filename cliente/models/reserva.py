from django.db import models
from cliente.models.cliente import Cliente
from carro.models.carro import Carro


class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente')
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING, related_name='carro')
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
