from django.db import models

from wagtail.wagtailcore.models import Page

# Create your models here.
class Recommendation(Page):
    parent_page_types = ['Recommendations']

class Recommendations(Page):
    subpage_types = ['Recommendation']
