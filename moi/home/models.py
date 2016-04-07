from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
     InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from core.models import HomeStreamBlock


class HomePage(Page):
    body_content = StreamField(HomeStreamBlock(), blank=True, null=True, default=None)

    search_fields = Page.search_fields + (
        index.SearchField('body_content'),
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body_content')
        #InlinePanel('top_stories', label="Top Stories"),
    ]

    subpage_types = ['about.About', 'carousel.Carousel', 'data.Data', 'sectors.Sector', 'data_gaps.DataGaps']

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

    content_panels = [
        FieldPanel('sector_name'),
        FieldPanel('top_stories_content'),
        MultiFieldPanel([
            FieldPanel('link_caption'),
            PageChooserPanel('url'),
        ]),
    ]

    class Meta:
        abstract = True


class HomePageTopStories(Orderable, TopStories):
    page = ParentalKey('HomePage', related_name='top_stories')
