# Generated by Django 5.0.1 on 2024-02-05 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0005_alter_indeed_job_list_custom_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeed_job_list',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='custom_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='date_of_post',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='job_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='job_title',
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='salary_range',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
