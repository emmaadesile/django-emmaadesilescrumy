# Generated by Django 2.0.4 on 2018-04-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emmascrumy', '0013_remove_scrumygoals_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumygoals',
            name='task_id',
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='task',
            field=models.TextField(blank=True),
        ),
    ]
