# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YSE_App', '0009_transient_tns_spec_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='transientphotdata',
            name='discovery_point',
            field=models.NullBooleanField(),
        ),
    ]
