# Generated by Django 4.2.7 on 2023-12-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_job_jobtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
