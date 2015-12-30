# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0010_change_on_delete_behaviour'),
        ('measures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coremeasure',
            name='displayTitle',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='coremeasure',
            name='image',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='coremeasure',
            name='main_content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='coremeasure',
            name='sub_title',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=None, null=True),
        ),
    ]
