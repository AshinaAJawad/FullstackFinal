# Generated by Django 5.0.6 on 2024-06-02 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0003_alter_medicine_times'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='times',
            new_name='time',
        ),
    ]
