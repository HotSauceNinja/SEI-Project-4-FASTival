# Generated by Django 3.1.5 on 2021-01-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling_slots', '0005_auto_20210127_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
