# Generated by Django 3.0.2 on 2020-01-21 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accomodation',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dashboard'),
        ),
    ]