# Generated by Django 5.0 on 2023-12-31 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='year',
            field=models.TextField(),
        ),
    ]
