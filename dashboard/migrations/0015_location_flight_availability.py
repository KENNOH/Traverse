# Generated by Django 3.0.2 on 2020-02-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_accomodation_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='flight_availability',
            field=models.NullBooleanField(default=1, max_length=5),
        ),
    ]
