# Generated by Django 3.1.7 on 2021-03-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo_salvador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turismosalvador',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='turismosalvador',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='turismosalvador',
            name='recomendado',
            field=models.BooleanField(default=False),
        ),
    ]
