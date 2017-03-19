# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-19 22:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0011_auto_20170317_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querytoken',
            name='date',
            field=models.DateField(default=datetime.date(2017, 3, 20)),
        ),
        migrations.AlterField(
            model_name='querytoken',
            name='query_type',
            field=models.CharField(choices=[('result', 'Result Discrepency'), ('credit', 'Credit Discrepency'), ('pdc_issue', 'Issue of PDC'), ('other_certificate', 'Issue of some other certificate')], db_index=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='querytoken',
            name='time',
            field=models.TimeField(default=datetime.time(3, 42, 33, 778655)),
        ),
    ]
