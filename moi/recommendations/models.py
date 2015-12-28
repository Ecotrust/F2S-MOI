from django.db import models

from wagtail.wagtailcore.models import Page

class Recommendation(Page):
    parent_page_types = ['indicators.Indicator']
    # subpage_types = []
    # page_type = models.CharField(default='Recommendation', max_length=255)

    class Meta:
        verbose_name = 'Recommendation'

    # def get_context(self, request):
    #     context = super(Recommendation, self).get_context(request)
    #
    #     context['base_page_type'] = 'Recommendation'
    #     return context
