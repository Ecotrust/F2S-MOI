from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class CoreMeasure(Page):
    parent_page_types = ['CoreMeasures']

class CoreMeasures(Page):
    subpage_types = ['CoreMeasure']
