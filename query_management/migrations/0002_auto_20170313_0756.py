# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-13 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('query_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querytoken',
            name='slot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='query_management.TimeSlot'),
        ),
    ]