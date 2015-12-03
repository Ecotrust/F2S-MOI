from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class Sector(Page):
    parent_page_types = ['Sectors']

class Sectors(Page):
    subpage_types = ['Sector']
