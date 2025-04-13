# Generated by Django 4.2.20 on 2025-04-13 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CEP', models.CharField(max_length=20)),
                ('Rua', models.CharField(max_length=100)),
                ('Bairro', models.CharField(max_length=100)),
                ('Estado', models.CharField(max_length=100)),
                ('Pais', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('Aniversario', models.DateField()),
                ('Data_Cadastro', models.DateField()),
                ('Aniversario_Cliente', models.DateField()),
                ('Ativo', models.BooleanField(default=True)),
                ('Classe_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tipo', to='Clientes.classe_cliente')),
                ('Endereco_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Endereco', to='Clientes.endereco')),
                ('Tipo_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tipo', to='Clientes.tipo_cliente')),
            ],
        ),
    ]
