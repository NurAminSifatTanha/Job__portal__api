# Generated by Django 3.1.5 on 2021-01-16 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210116_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]