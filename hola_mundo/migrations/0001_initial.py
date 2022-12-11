# Generated by Django 3.2.14 on 2022-12-11 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('cuit', models.CharField(max_length=150, verbose_name='CUIT')),
                ('legajo', models.CharField(max_length=100, verbose_name='Legajo')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripcion')),
                ('nombreprov', models.ManyToManyField(to='hola_mundo.Clientes')),
            ],
        ),
    ]