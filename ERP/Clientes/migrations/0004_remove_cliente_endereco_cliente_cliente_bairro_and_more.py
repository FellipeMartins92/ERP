# Generated by Django 4.2.20 on 2025-04-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clientes', '0003_alter_cliente_classe_cliente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='Endereco_Cliente',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Bairro',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='CEP',
            field=models.CharField(default='22', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Estado',
            field=models.CharField(default='12', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Pais',
            field=models.CharField(default='12', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='Rua',
            field=models.CharField(default='12', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
