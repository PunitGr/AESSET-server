# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0009_auto_20170317_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querytoken',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='querytoken',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
