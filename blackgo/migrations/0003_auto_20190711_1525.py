# Generated by Django 2.2.2 on 2019-07-11 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blackgo', '0002_blackgouniventerance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blackgouniventerance',
            old_name='univ_enterance_name',
            new_name='univ_entrance_name',
        ),
        migrations.RenameField(
            model_name='blackgouniventerance',
            old_name='univ_enterance_type',
            new_name='univ_entrance_type',
        ),
    ]