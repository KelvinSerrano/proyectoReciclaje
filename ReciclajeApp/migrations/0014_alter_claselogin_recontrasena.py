# Generated by Django 5.1.2 on 2024-10-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReciclajeApp', '0013_claselogin_recontrasena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claselogin',
            name='recontrasena',
            field=models.CharField(max_length=50),
        ),
    ]
