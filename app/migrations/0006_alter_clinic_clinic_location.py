# Generated by Django 3.2.4 on 2021-06-25 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_clinic_address_clinic_clinic_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='clinic_location',
            field=models.URLField(),
        ),
    ]