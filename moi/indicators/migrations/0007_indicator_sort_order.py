# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 21:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0006_auto_20160322_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
