# Generated by Django 3.1.5 on 2021-01-15 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210115_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('Other', 'O'), ('Full Time', 'F'), ('Part Time', 'P')], max_length=255),
        ),
    ]
