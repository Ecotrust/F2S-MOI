from __future__ import unicode_literals

from django.db import models
from django.utils.safestring import mark_safe

from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

from modelcluster.fields import ParentalKey

class Menu(models.Model):
    class Meta:
        ordering = ('footer', 'order',)

    title = models.CharField(max_length=255)
    url = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        help_text="Internal path to specific page",
    )
    footer = models.BooleanField(default=False, help_text=("Select to display "
       "this menu in the footer rather than in the nav bar."))
    order = models.PositiveSmallIntegerField(default=1, help_text=("The "
        "order that this menu appears. Lower numbers appear first."))

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            PageChooserPanel('url'),
            FieldPanel('footer'),
            FieldPanel('order'),
        ]),
    ]

    def __unicode__(self):
        if self.footer:
            position = 'Footer'
        else:
            position = 'Navbar'

        s = '%s %d. <b>%s</b>' % (position, self.order, self.title)
        return mark_safe(s)

register_snippet(Menu)
