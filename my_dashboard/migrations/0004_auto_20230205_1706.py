# Generated by Django 3.2.17 on 2023-02-05 20:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_dashboard', '0003_auto_20230205_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_despesa', models.CharField(max_length=50)),
                ('total', models.FloatField()),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 2, 5, 17, 6, 3, 914974))),
            ],
        ),
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 5, 17, 6, 3, 914540)),
        ),
    ]
