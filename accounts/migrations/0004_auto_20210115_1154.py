# Generated by Django 3.1.5 on 2021-01-15 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_graduate_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='last_education',
            new_name='degree_name',
        ),
    ]
