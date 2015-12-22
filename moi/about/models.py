from django.db import models

from wagtail.wagtailcore.models import Page

class About(Page):
    parent_page_types = ['home.HomePage']
