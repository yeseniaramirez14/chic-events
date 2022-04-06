# Generated by Django 4.0.3 on 2022-04-06 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_rename_comment_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('phone_number', models.CharField(max_length=20)),
                ('guests', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='package_type', to='events.event')),
            ],
        ),
    ]