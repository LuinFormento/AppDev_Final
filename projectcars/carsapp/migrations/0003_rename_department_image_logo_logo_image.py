# Generated by Django 5.0 on 2023-12-31 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0002_alter_car_model_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logo',
            old_name='department_image',
            new_name='logo_image',
        ),
    ]
