# Generated by Django 2.0.4 on 2019-11-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0042_remove_surveyobservation_instrument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyobservation',
            name='pos_angle_deg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]