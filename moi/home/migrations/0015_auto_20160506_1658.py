# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 16:58
from __future__ import unicode_literals

import core.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20160504_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_content',
            field=wagtail.wagtailcore.fields.StreamField([(b'number_count_up', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter your main content above. Do not use commas for larger numbers.', label=b'Text')), (b'numbers', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the numbers you'd like to count up - seperated by a semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label=b'Numbers to count', required=False)), (b'colored_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the content you'd like to be a different color - each set of content is seperated by a semicolon", required=False)), (b'source', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter a source for the associated information.', required=False))], icon=b'order', label=b'Content and Number Counter Block')), (b'top_story', wagtail.wagtailcore.blocks.StructBlock([(b'sector', core.models.SectorChoiceBlock(help_text=b'Select the sector/top-story this aligns with')), (b'content', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter your main content above. Do not use commas for larger numbers.', label=b'Text')), (b'numbers', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the numbers you'd like to count up - seperated by a semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label=b'Numbers to count', required=False)), (b'colored_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the content you'd like to be a different color - each set of content is seperated by a semicolon", required=False)), (b'source', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter a source for the associated information.', required=False))])), (b'link_caption', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Add the text you would like to display that will link to the sector page', label=b'Link text')), (b'source', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Display your source here', required=False))], icon=b'title', label=b'Top Story Content Block')), (b'basic_content', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Add your text and/or image content above', label=b'Content Area'))], icon=b'pilcrow', label=b'Basic Content Block'))], blank=True, default=None, null=True),
        ),
    ]
