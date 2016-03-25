from django.db import models
from django import forms
from django.template.loader import render_to_string

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
     InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, \
     ChoiceBlock, RichTextBlock, RawHTMLBlock, BooleanBlock, PageChooserBlock, URLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock

from modelcluster.fields import ParentalKey

#Streamfields

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"

class SectorChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('education', 'Education'), ('health', 'Health'), ('economy', 'Economy'), ('environment', 'Environment'), ('data_gaps', 'Data Gaps'),
    ))

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"

class BasicContentBlock(StructBlock):
    content = RichTextBlock(help_text="Add your text and/or image content above", label="Content Area")

    class Meta:
        template = "blocks/basic_content_block.html"


class NumberCountUpBlock(StructBlock):
    content = RichTextBlock(help_text="Enter your main content above. Do not use commas for larger numbers.", label="Text")
    numbers = CharBlock(required=False, help_text="Enter the numbers you'd like to count up - seperated by a semicolon. Do not use commas for larger numbers. Ex: 4; 51000; 15", label="Numbers to count")
    colored_text = CharBlock(required=False, help_text="Enter the content you'd like to be a different color - each set of content is seperated by a semicolon")
    inline = BooleanBlock(required=False, help_text="If this is not a standalone number, but apart of an actual sentence - check the box.")

    def render(self, value):
        num = value['numbers']
        current_context = value['content'].source
        inline = value['inline']
        colored = value['colored_text']

        if colored:
            colored_list = colored.split("; ")
            #add color wrapper to identified content
            for color in colored_list:
                color_span = "<span class='color-text'>%s</span>" % (color)  
                current_context = current_context.replace(color, color_span, 1)

        if num:
            num_list = num.split("; ")
            # add count-up functionality to identified numbers
            for num in num_list:                    
                html_span = "<span id='count-%s' class='count-up'></span>" % (num)                                                          
                current_context = current_context.replace(num, html_span, 1)
        else:
            num_list = None

        return render_to_string(self.meta.template, {
            'self': value,
            'content': current_context,
            'numbers': num_list,
            'inline': inline,

        })

    class Meta:
        template = "blocks/number_count_up_block.html"


class TopStoryBlock(StructBlock):
    sector = SectorChoiceBlock(help_text="Select the sector/top-story this aligns with")
    content = NumberCountUpBlock()
    link_caption = CharBlock(help_text="Add the text you would like to display that will link to the sector page", label="Link text")
    source = RichTextBlock(required=False, help_text="Display your source here")

    class Meta:
        template = "blocks/top_story_block.html"


class TwoColumnBlock(StructBlock):

    left_column = StreamBlock([
            ('heading', CharBlock(icon="title", classname="full title")),
            ('paragraph', RichTextBlock(icon="pilcrow")),
            ('number_count_up', NumberCountUpBlock(icon="collapse-up")),
            ('image', ImageChooserBlock(icon="image")),
            # ('embedded_video', EmbedBlock(icon="media")),
        ], icon='arrow-left', label='Left content')

    right_column = StreamBlock([
            ('heading', CharBlock(icon="title", classname="full title")),
            ('paragraph', RichTextBlock(icon="pilcrow")),
            ('number_count_up', NumberCountUpBlock(icon="collapse-up")),
            ('image', ImageChooserBlock(icon="image")),
            # ('embedded_video', EmbedBlock(icon="media")),
        ], icon='arrow-right', label='Right content')

    class Meta:
        template = 'blocks/two_column_block.html'
        icon = 'placeholder'
        label = 'Two Columns'

class CoreStreamBlock(StreamBlock):
    number_count_up = NumberCountUpBlock(icon="order", label="Content and Number Counter Block")
    basic_content = BasicContentBlock(icon="pilcrow", label="Basic Content Block")
    # aligned_image = ImageBlock(label="Aligned image", icon="image")
    # aligned_html = AlignedHTMLBlock(icon="code", label='Raw HTML')
    # document = DocumentChooserBlock(icon="doc-full-inverse")
    # embedded_video = EmbedBlock(icon="media")
    two_column = TwoColumnBlock()

class HomeStreamBlock(StreamBlock):
    number_count_up = NumberCountUpBlock(icon="order", label="Content and Number Counter Block")
    top_story = TopStoryBlock(icon='title', label="Top Story Content Block")
    basic_content = BasicContentBlock(icon="pilcrow", label="Basic Content Block")

