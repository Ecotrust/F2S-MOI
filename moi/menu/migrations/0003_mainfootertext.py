# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-22 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160121_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainFooterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(help_text="Header text to display above text. Ex. 'Welcome'", max_length=100)),
                ('content', wagtail.wagtailcore.fields.RichTextField(blank=True)),
            ],
        ),
    ]
