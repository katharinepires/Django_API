# Generated by Django 3.1.7 on 2021-04-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0004_auto_20210401_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacao',
            name='endereco',
            field=models.CharField(max_length=100),
        ),
    ]
