# Generated by Django 3.1.7 on 2021-04-02 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo_salvador', '0011_auto_20210401_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='turismosalvador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='turismo_salvador'),
        ),
    ]