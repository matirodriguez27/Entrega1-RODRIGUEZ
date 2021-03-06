# Generated by Django 4.0.4 on 2022-06-06 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombre', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Ciudadano',
        ),
        migrations.RemoveField(
            model_name='desecho',
            name='reciclable',
        ),
        migrations.RemoveField(
            model_name='estacion',
            name='id',
        ),
        migrations.RemoveField(
            model_name='estacion',
            name='unidadNumero',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticketid',
        ),
        migrations.AddField(
            model_name='estacion',
            name='idEstacion',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='idTicket',
            field=models.IntegerField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='usuarioAsociado',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
