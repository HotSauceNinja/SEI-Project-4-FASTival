# Generated by Django 3.1.5 on 2021-01-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20210127_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.CharField(max_length=100),
        ),
    ]
