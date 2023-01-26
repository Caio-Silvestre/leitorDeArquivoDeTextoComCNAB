# Generated by Django 4.1.5 on 2023-01-25 13:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HandleCnab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeOperations', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)])),
                ('data', models.DateTimeField()),
                ('valor', models.FloatField()),
                ('cpf', models.IntegerField()),
                ('cartao', models.IntegerField()),
                ('hora', models.TimeField()),
                ('donoDaLoja', models.CharField(max_length=200)),
                ('nomeDaLoja', models.CharField(max_length=200)),
            ],
        ),
    ]