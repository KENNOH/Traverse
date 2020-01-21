# Generated by Django 3.0.2 on 2020-01-20 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('urlhash', models.CharField(blank=True, max_length=6, null=True)),
                ('contact_email', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='dashboard')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Accomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('urlhash', models.CharField(blank=True, max_length=6, null=True)),
                ('rooms', models.CharField(blank=True, max_length=255, null=True)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('people', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('cost', models.FloatField(default=0.0)),
                ('status', models.NullBooleanField(default=0, max_length=5, verbose_name='Available')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
