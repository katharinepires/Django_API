# Generated by Django 3.1.7 on 2021-03-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='localizacao',
            name='ponto_referencia',
            field=models.CharField(default='', max_length=100),
        ),
    ]
