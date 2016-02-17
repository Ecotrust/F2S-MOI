from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailsearch import index

from core.models import CoreStreamBlock

class CoreMeasure(Page):
    DATA_CHOICES = (
        ('pie', 'Pie'),
        ('bar', 'Bar'),
        ('line', 'Line'),
        ('number', 'Number'),
    )

    display_title = RichTextField(blank=True)
    body_content = StreamField(CoreStreamBlock(), blank=True, null=True, default=None)
    data_viz_type = models.CharField(choices=DATA_CHOICES,
                                    max_length=1,
                                    null=True,
                                    default=None,
                                    help_text='Select the type of data vizulation for this Core Measure')

    search_fields = Page.search_fields + (
            index.SearchField('display_title'),
            index.SearchField('body_content'),
       )

    content_panels = Page.content_panels + [
        FieldPanel('display_title'),
        FieldPanel('data_viz_type'),
        StreamFieldPanel('body_content'),
    ]

    parent_page_types = ['indicators.Indicator']

    class Meta:
        verbose_name = "Core Measure"
