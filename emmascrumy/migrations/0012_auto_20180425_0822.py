# Generated by Django 2.0.4 on 2018-04-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emmascrumy', '0011_auto_20180421_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goalstatus',
            options={'verbose_name_plural': 'GoalStatus'},
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='task_id',
            field=models.IntegerField(default=10),
        ),
    ]
