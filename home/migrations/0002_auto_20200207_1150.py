# Generated by Django 3.0.2 on 2020-02-07 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20200207_1039'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='package',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Accomodation'),
        ),
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.NullBooleanField(default=1, max_length=5, verbose_name='Payment status'),
        ),
    ]
