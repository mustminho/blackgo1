# Generated by Django 2.2.2 on 2019-07-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackgo', '0004_blackgoonlineacademy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackgoonlineacademy',
            name='offline_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]