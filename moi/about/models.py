from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailsearch import index

from core.models import CoreStreamBlock

class About(Page):
    parent_page_types = ['home.HomePage']
    body_content = StreamField(CoreStreamBlock(), blank=True, null=True, default=None)

    search_fields = Page.search_fields + [
        index.SearchField('body_content'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body_content'),
    ]
