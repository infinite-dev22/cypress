# Generated by Django 4.1.5 on 2023-03-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='description',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='time_slot',
        ),
        migrations.AlterField(
            model_name='timetable',
            name='year',
            field=models.IntegerField(default=2023),
        ),
    ]
