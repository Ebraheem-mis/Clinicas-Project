# Generated by Django 3.2.4 on 2021-06-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='clinic_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='clinic_phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_phone',
            field=models.IntegerField(),
        ),
    ]
