# Generated by Django 4.2.7 on 2023-12-04 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_experience_slug_gender_slug_jobtype_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='jobtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jobs.jobtype'),
        ),
    ]