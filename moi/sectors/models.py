from django.db import models

from wagtail.wagtailcore.models import Page

class Sector(Page):
    parent_page_types = ['data.Data']
    subpage_types = ['outcomes.PriorityOutcome']
