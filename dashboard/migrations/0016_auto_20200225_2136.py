# Generated by Django 3.0.2 on 2020-02-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_location_flight_availability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='flight_availability',
            field=models.NullBooleanField(default=0, max_length=5),
        ),
    ]
