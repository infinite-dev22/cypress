# Generated by Django 4.1.5 on 2023-02-26 15:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('assessment', '0005_alter_result_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='test_1',
            new_name='test',
        ),
    ]
