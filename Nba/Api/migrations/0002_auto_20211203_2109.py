# Generated by Django 3.2.9 on 2021-12-03 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='height_in',
            new_name='h_in',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='meters_h',
            new_name='h_meters',
        ),
    ]
