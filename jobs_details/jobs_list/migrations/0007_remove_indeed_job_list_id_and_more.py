# Generated by Django 5.0.1 on 2024-02-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0006_alter_indeed_job_list_company_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indeed_job_list',
            name='id',
        ),
        migrations.AlterField(
            model_name='indeed_job_list',
            name='custom_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]