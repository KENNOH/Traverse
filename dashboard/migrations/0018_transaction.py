# Generated by Django 3.0.2 on 2020-03-03 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0017_auto_20200303_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mpesa_receipt_number', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.FloatField(default=0.0, max_length=30, verbose_name='Amount transacted')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('status', models.NullBooleanField(default=1, max_length=5)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Initiated By')),
            ],
        ),
    ]
