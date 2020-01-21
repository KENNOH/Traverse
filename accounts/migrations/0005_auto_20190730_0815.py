# Generated by Django 2.2.3 on 2019-07-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190730_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(choices=[('Public Transport', 'Public Transport'), ('County Public Service Board', 'County Public Service Board'), ('Water And Environment', 'Water And Environment'), ('Education And Sports', 'Education And Sports'), ('Trade', 'Trade'), ('Agriculture', 'Agriculture'), ('Public Administration', 'Public Administration'), ('Gender And Social Services', 'Gender And Social Services'), ('Health', 'Health'), ('Economic Planning', 'Economic Planning'), ('Lands And Housing', 'Lands And Housing'), ('Finance', 'Finance'), ('County Secretary', 'County Secretary'), ('Governor And Deputy Governor', 'Governor And Deputy Governor')], max_length=30, verbose_name='Department'),
        ),
    ]
