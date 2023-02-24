from django.db import models
from cliente.models.local import Local
from cliente.models.reserva import Reserva


class Entrega(models.Model):
    reserva = models.OneToOneField(Reserva, on_delete=models.DO_NOTHING, related_name='reserva')
    local = models.ForeignKey(Local, on_delete=models.DO_NOTHING, related_name='local')
    data_entrega = models.DateTimeField()
