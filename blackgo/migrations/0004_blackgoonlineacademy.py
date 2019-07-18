# Generated by Django 2.2.2 on 2019-07-11 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackgo', '0003_auto_20190711_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlackgoOnlineAcademy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('site_description', models.CharField(max_length=200)),
                ('site_url', models.URLField()),
                ('offline_url', models.URLField(null=True)),
            ],
        ),
    ]
