# Generated by Django 5.0.1 on 2024-01-28 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0020_delete_contact_delete_job_list_delete_sign_up'),
    ]

    operations = [
        migrations.CreateModel(
            name='adm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
