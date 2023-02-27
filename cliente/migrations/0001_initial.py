# Generated by Django 4.1.7 on 2023-02-24 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=14)),
                ('endereco', models.CharField(max_length=400)),
                ('telefone', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cep', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='carro_reserva', to='carro.carro')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente_reserva', to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrega', models.DateTimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='local_entrega', to='cliente.local')),
                ('reserva', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reserva_entrega', to='cliente.reserva')),
            ],
        ),
    ]