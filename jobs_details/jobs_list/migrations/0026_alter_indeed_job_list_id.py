# Generated by Django 5.0.1 on 2024-02-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_list', '0025_indeed_job_list_company_indeed_job_list_date_of_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indeed_job_list',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
