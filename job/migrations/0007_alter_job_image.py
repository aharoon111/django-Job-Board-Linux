# Generated by Django 4.0.4 on 2022-05-10 15:07

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_alter_job_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, height_field=80, null=True, upload_to=job.models.image_upload, width_field=80),
        ),
    ]
