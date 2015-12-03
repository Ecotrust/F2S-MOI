from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class Indicator(Page):
    parent_page_types = ['Indicators']

class Indicators(Page):
    subpage_types = ['Indicator']
