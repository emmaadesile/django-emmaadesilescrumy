# Generated by Django 2.0.4 on 2018-04-21 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('emmascrumy', '0010_auto_20180421_1720'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goalstatus',
            options={'verbose_name_plural': 'ScrumyStatus'},
        ),
        migrations.AlterModelOptions(
            name='scrumygoals',
            options={'verbose_name_plural': 'ScrumyGoals'},
        ),
        migrations.AlterModelOptions(
            name='scrumyuser',
            options={'verbose_name_plural': 'ScrumyUser'},
        ),
        migrations.AlterField(
            model_name='goalstatus',
            name='status',
            field=models.CharField(choices=[('WT', 'Weekly Task'), ('DT', 'Daily Task'), ('V', 'Verified'), ('D', 'Done')], default='DT', max_length=50),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
