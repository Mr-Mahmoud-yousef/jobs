# Generated by Django 3.1.5 on 2021-01-31 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
