# Generated by Django 4.2.6 on 2023-10-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
