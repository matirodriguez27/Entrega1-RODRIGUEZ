# Generated by Django 4.0.4 on 2022-06-07 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0005_alter_aparicion_superhumano'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Desecho',
        ),
        migrations.DeleteModel(
            name='Estacion',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
