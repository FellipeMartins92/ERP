# Generated by Django 4.2.20 on 2025-04-13 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Aniversario',
        ),
    ]
