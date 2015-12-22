from django.db import models

from wagtail.wagtailcore.models import Page

class PriorityOutcome(Page):
    parent_page_types = ['sectors.Sector']
    subpage_types = ['indicators.Indicator']
