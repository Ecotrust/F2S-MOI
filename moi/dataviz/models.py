from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class DataVisualization(Page):
    parent_page_types = ['DataVisualizations']

class DataVisualizations(Page):
    subpage_types = ['DataVisualization']
