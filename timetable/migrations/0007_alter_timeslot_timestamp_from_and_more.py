# Generated by Django 4.1.5 on 2023-03-04 10:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timetable', '0006_alter_timeslot_timestamp_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='timestamp_from',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='timestamp_to',
            field=models.TimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
