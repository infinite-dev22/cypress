# Generated by Django 4.1.5 on 2023-03-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timetable', '0003_remove_timetable_day_of_week_remove_timetable_exam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='time_slot',
            field=models.ManyToManyField(blank=True, default=None, to='timetable.timeslot'),
        ),
    ]
