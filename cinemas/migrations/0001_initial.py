# Generated by Django 3.1.5 on 2021-01-27 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=500)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('phone_number', models.CharField(max_length=14)),
                ('contact_name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]