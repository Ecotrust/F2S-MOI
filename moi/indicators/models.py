from django.db import models

from wagtail.wagtailcore.models import Page

class Indicator(Page):
    parent_page_types = ['outcomes.PriorityOutcome']
    subpage_types = ['measures.CoreMeasure', 'recommendations.Recommendation']
