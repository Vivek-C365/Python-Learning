# Generated by Django 5.0.1 on 2024-02-06 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0030_rename_sid_indeed_job_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeed_job_list',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
