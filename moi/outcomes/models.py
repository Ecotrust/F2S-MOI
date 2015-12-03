from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class PriorityOutcome(Page):
    parent_page_types = ['PriorityOutcomes']

class PriorityOutcomes(Page):
    subpage_types = ['PriorityOutcome']
