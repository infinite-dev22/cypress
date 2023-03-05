# Generated by Django 4.1.5 on 2023-03-04 13:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timetable', '0013_alter_timetablerecord_day_of_week'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetablerecord',
            name='time_slot',
        ),
        migrations.AddField(
            model_name='timetablerecord',
            name='time_slot',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='timetable.timeslot'),
        ),
    ]
