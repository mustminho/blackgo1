# Generated by Django 2.2.2 on 2019-07-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackgoCafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_name', models.CharField(max_length=100)),
                ('cafe_url', models.URLField(verbose_name='Cafe URL')),
                ('cafe_description', models.CharField(max_length=200)),
            ],
        ),
    ]
