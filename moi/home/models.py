from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index


class HomePage(Page):
    display_title = RichTextField(blank=True)
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

    search_fileds = Page.search_fields + (
        index.SearchField('display_title'),
        index.SearchField('sub_title'),
        index.SearchField('main_content'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('display_title'),
        FieldPanel('sub_title', classname="subtitle or blurb"),
        FieldPanel('main_content', classname="content"),
        ImageChooserPanel('image'),
        InlinePanel('top_stories', label="Top Stories"),
    ]

    subpage_types = ['about.About', 'carousel.Carousel', 'data.Data']

#Top Stories
class TopStories(models.Model):
    sector_name = RichTextField(blank=True, help_text="Sector Name - Headline")
    top_stories_content = RichTextField(blank=True, help_text="Main content field for top stories")
    link_caption = models.CharField(max_length=250, help_text="Text for clickable links to specific sector")
    url = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        help_text="Internal path to specific sector",
    )

    panels = [
        FieldPanel('sector_name'),
        FieldPanel('top_stories_content'),
        FieldPanel('link_caption'),
        PageChooserPanel('url'),
    ]

    class Meta:
        abstract = True


class HomePageTopStories(Orderable, TopStories):
    page = ParentalKey('HomePage', related_name='top_stories')
