# Generated by Django 3.1.3 on 2020-11-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_auto_20201122_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
