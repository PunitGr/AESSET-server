# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-05 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0002_auto_20170217_0334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='token',
            new_name='token_id',
        ),
    ]