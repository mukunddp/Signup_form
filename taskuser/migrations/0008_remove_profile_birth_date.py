# Generated by Django 4.0.3 on 2022-04-07 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskuser', '0007_remove_profile_image_studentprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
    ]
