# Generated by Django 5.2 on 2025-04-21 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
