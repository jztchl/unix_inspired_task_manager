# Generated by Django 5.2 on 2025-04-21 14:40

import task.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=task.models.StatusChoices['PENDING'], max_length=20),
        ),
    ]
