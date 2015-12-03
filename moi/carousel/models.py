from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class Carousel(Page):
    parent_page_types = ['Carousels']

class Carousels(Page):
    subpage_types = ['Carousel']
