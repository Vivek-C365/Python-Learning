# Generated by Django 5.0.1 on 2024-02-06 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0011_alter_indeed_job_list_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indeed_job_list',
            old_name='id',
            new_name='custom_id',
        ),
    ]
