# Generated by Django 4.0.3 on 2022-04-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_bookrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='members',
        ),
    ]
