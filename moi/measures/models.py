from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.wagtailsearch import index

from data.models import Data as DV

from core.models import BasicContentBlock

class RelatedData(DV):
    content_panels = [ MultiFieldPanel(DV.content_panels, 'Data'), ]

    class Meta:
        abstract = True


class CoreMeasure(Page):
    display_title = RichTextField(blank=True)
    body_content = RichTextField(blank=True, null=True, default=None, verbose_name="Extra Content")

    search_fields = Page.search_fields + (
            index.SearchField('display_title'),
            index.SearchField('body_content'),
       )

    content_panels = Page.content_panels + [
        FieldPanel('display_title'),
        InlinePanel('related_data', label='Data'),
        FieldPanel('body_content'),
    ]

    parent_page_types = ['indicators.Indicator']

    class Meta:
        verbose_name = "Core Measure"


class CoreMeasureRelatedData(RelatedData):
    page = ParentalKey('CoreMeasure', related_name='related_data')
