# Generated by Django 4.1.5 on 2023-02-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('echelon', '0004_alter_term_ends_on_alter_term_starts_on'),
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exammaster',
            name='classes',
            field=models.ManyToManyField(to='echelon.class'),
        ),
    ]
