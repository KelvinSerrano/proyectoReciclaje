# Generated by Django 4.2.7 on 2023-11-24 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReciclajeApp', '0002_claseincentivos'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NumeroCuenta', models.CharField(max_length=50)),
                ('Banco', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=50)),
                ('Rut', models.CharField(max_length=50)),
                ('Correo', models.CharField(max_length=15)),
            ],
        ),
    ]
