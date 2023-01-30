# Generated by Django 4.1.5 on 2023-01-24 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0005_bursar_headteacher_librarian_parent_delete_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='baseuser',
            name='user_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.usertype'),
        ),
    ]
