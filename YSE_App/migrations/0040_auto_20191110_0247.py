# Generated by Django 2.0.4 on 2019-11-10 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0039_surveyfield_ztf_field_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyobservationtask',
            name='date_requested',
        ),
        migrations.AddField(
            model_name='surveyobservationtask',
            name='mjd_requested',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
