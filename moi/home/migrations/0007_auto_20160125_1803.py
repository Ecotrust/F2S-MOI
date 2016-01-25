# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 18:03
from __future__ import unicode_literals

import core.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160122_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_content',
            field=wagtail.wagtailcore.fields.StreamField([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'number_count_up', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter your main content above. Do not use commas for larger numbers.', label=b'Text')), (b'numbers', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the numbers you'd like to count up - seperated by semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label=b'Numbers to count'))], icon=b'collapse-up', label=b'Content and Number Count Up')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'alignment', core.models.ImageFormatChoiceBlock())], icon=b'image', label=b'Aligned image')), (b'aligned_html', wagtail.wagtailcore.blocks.StructBlock([(b'html', wagtail.wagtailcore.blocks.RawHTMLBlock()), (b'alignment', core.models.HTMLAlignmentChoiceBlock())], icon=b'code', label=b'Raw HTML')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon=b'doc-full-inverse')), (b'embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media')), (b'two_column', wagtail.wagtailcore.blocks.StructBlock([(b'left_column', wagtail.wagtailcore.blocks.StreamBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'number_count_up', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter your main content above. Do not use commas for larger numbers.', label=b'Text')), (b'numbers', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the numbers you'd like to count up - seperated by semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label=b'Numbers to count'))], icon=b'collapse-up')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media'))], icon=b'arrow-left', label=b'Left content')), (b'right_column', wagtail.wagtailcore.blocks.StreamBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title', icon=b'title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'pilcrow')), (b'number_count_up', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter your main content above. Do not use commas for larger numbers.', label=b'Text')), (b'numbers', wagtail.wagtailcore.blocks.CharBlock(help_text=b"Enter the numbers you'd like to count up - seperated by semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label=b'Numbers to count'))], icon=b'collapse-up')), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock(icon=b'media'))], icon=b'arrow-right', label=b'Right content'))]))], blank=True, default=None, null=True),
        ),
    ]
