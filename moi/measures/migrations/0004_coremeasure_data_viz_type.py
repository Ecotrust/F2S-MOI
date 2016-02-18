# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measures', '0003_auto_20160130_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='coremeasure',
            name='data_viz_type',
            field=models.CharField(choices=[(b'pie', b'Pie'), (b'bar', b'Bar'), (b'line', b'Line'), (b'number', b'Number')], default=None, help_text=b'Select the type of data vizulation for this Core Measure', max_length=1, null=True),
        ),
    ]
