# Generated by Django 4.1.5 on 2023-03-04 11:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timetable', '0009_alter_timeslot_timestamp_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeslot',
            name='meridian_from',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='meridian_to',
            field=models.CharField(max_length=3),
        ),
    ]
