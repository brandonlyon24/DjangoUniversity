# Generated by Django 3.1.4 on 2020-12-20 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='duration',
            field=models.FloatField(blank=True, default=''),
        ),
    ]
