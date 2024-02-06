# Generated by Django 5.0.1 on 2024-02-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0021_alter_indeed_job_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeed_job_list',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='job_title',
            field=models.CharField(max_length=123),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='salary_range',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='tags',
            field=models.CharField(max_length=100),
        ),
    ]
