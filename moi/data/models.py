from django.db import models

from wagtail.wagtailcore.models import Page

class Data(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['sectors.Sector']
