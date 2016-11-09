from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.wagtailsearch import index

from core.models import CoreStreamBlock

class PriorityOutcome(Page, Orderable):
    display_title = RichTextField(blank=True)
    body_content = StreamField(CoreStreamBlock(), blank=True, null=True, default=None)

    search_fields = Page.search_fields + [
            index.SearchField('display_title'),
            index.SearchField('body_content'),
       ]

    content_panels = Page.content_panels + [
        FieldPanel('display_title'),
        StreamFieldPanel('body_content'),
    ]

    parent_page_types = ['sectors.Sector']
    subpage_types = ['indicators.Indicator']
