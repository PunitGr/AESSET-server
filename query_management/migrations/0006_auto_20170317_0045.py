# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0005_auto_20170316_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querytoken',
            name='status',
            field=models.CharField(choices=[('resolved', 'Resolved'), ('unresolved', 'Unresolved'), ('pending', 'Pending'), ('reschedule', 'Reschedule'), ('transfer', 'Transfered to other department')], default='unresolved', max_length=24),
        ),
    ]
