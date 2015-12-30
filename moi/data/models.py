from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class Data(Page):
    displayTitle = RichTextField(blank=True)
    sub_title = RichTextField(blank=True, null=True, default=None)
    main_content = RichTextField(blank=True, null=True, default=None)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('displayTitle', classname="full"),
        FieldPanel('sub_title', classname="subtitle or blurb"),
        FieldPanel('main_content', classname="content"),
        ImageChooserPanel('image')
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = ['sectors.Sector']
