# Generated by Django 3.2.4 on 2021-06-25 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210624_2021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='clinic_email',
            new_name='doctor_email',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='clinic_phone',
            new_name='doctor_phone',
        ),
    ]