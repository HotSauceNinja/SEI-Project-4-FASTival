# Generated by Django 3.1.5 on 2021-01-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('films', '0003_auto_20210127_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(related_name='films', to='genres.Genre'),
        ),
    ]
