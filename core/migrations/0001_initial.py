# Generated by Django 5.2.1 on 2025-05-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]
