# Generated by Django 3.1.7 on 2021-03-30 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0003_auto_20210330_1933'),
        ('turismo_salvador', '0008_auto_20210330_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turismosalvador',
            name='localizacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizacao.localizacao'),
        ),
    ]