# Generated by Django 5.1.2 on 2024-12-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReciclajeApp', '0015_alter_claselogin_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claselogin',
            old_name='contrasena',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='claselogin',
            old_name='correo',
            new_name='username',
        ),
    ]