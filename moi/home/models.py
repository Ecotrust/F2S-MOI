from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    displayTitle = RichTextField(blank=True)
    # parent_page_types = ['HomePage']

    content_panels = Page.content_panels + [
        FieldPanel('displayTitle', classname="full")
    ]



# class
