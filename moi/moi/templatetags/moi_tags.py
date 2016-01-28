from django import template

from collections import OrderedDict

from sectors.models import Sector
from outcomes.models import PriorityOutcome
from indicators.models import Indicator
from measures.models import CoreMeasure
from home.models import HomePageTopStories

register = template.Library()

@register.inclusion_tag('moi/content_taxonomy.html')
def display_sectors():
    sectors = Sector.objects.all()
    outcomes = PriorityOutcome.objects.all()
    indicators = Indicator.objects.all()
    measures = CoreMeasure.objects.all()

    for sector in sectors:
        if 'education' in sector.title.lower():
            ed_sector = sector
        elif 'environment' in sector.title.lower():
            env_sector = sector
        elif 'health' in sector.title.lower():
            health_sector = sector
        else:
            eco_sector = sector

    sectors = [eco_sector, ed_sector, health_sector, env_sector]        


    return {
        'sectors': sectors,
        'outcomes': outcomes,
        'indicators': indicators,
        'measures': measures,
    }