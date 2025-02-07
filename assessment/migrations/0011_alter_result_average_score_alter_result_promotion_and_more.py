# Generated by Django 4.1.5 on 2023-03-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('assessment', '0010_remove_result_subject_result_average_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='average_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='promotion',
            field=models.SmallIntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
        migrations.AlterField(
            model_name='result',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
