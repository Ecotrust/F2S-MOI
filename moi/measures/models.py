from django.db import models

from wagtail.wagtailcore.models import Page

class CoreMeasure(Page):
    parent_page_types = ['indicators.Indicator']
    subpage_types = []
    page_type = models.CharField(default='Core Measure', max_length=255)

    class Meta:
        verbose_name = "Core Measure"

    def get_context(self, request):
        context = super(CoreMeasure, self).get_context(request)

        context['base_page_type'] = ['Core Measure']
        return context
