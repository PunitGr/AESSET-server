# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-25 03:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0015_auto_20170325_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querytoken',
            name='time',
            field=models.TimeField(default=datetime.time(8, 59, 54, 337780)),
        ),
    ]
