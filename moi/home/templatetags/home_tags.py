from django import template
from sectors.models import Sector

register = template.Library()

@register.inclusion_tag('home/sectors.html')
def display_sectors():
    sectors = Sector.objects.all()
    return {'sectors': sectors}