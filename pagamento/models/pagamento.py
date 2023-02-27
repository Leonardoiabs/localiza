from django.db import models
from cliente.models.reserva import Reserva


class Pagamento(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.DO_NOTHING, related_name='reserva_pagamento')
    forma_pagamento = models.CharField(max_length=100)
    valor = models.IntegerField()
    data_pagamento = models.DateTimeField()
