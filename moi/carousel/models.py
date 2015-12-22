from django.db import models

from wagtail.wagtailcore.models import Page

class Carousel(Page):
    parent_page_types = ['Carousels', 'home.HomePage']

class Carousels(Page):
    subpage_types = []
