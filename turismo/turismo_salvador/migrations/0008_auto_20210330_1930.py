# Generated by Django 3.1.7 on 2021-03-30 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0002_localizacao_ponto_referencia'),
        ('turismo_salvador', '0007_auto_20210330_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turismosalvador',
            name='localizacao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]