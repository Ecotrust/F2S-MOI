from django import template
from django.template.loader import get_template

from wagtail.wagtailimages.models import Image

from menu.models import Menu, MainFooterText
from home.models import HomePage

register = template.Library()

def logo():
    image = Image.objects.filter(tags__name__in=["navbar"]).first()
    if image:
        return image.file.url
    else:
        return None

@register.simple_tag(takes_context=True)
def menus(context, kind='header', menu_type='navbar'):

    t = get_template("menu/tags/%s.html" % menu_type)

    footer = (kind == 'footer')
    menus = Menu.objects.filter(footer=footer)
    navbar_logo = logo()

    return t.render(template.Context({
        'menus': menus,
        'navbar_logo': navbar_logo,
        'request': context['request'],
}))

@register.assignment_tag
def footer_menus():
    return Menu.objects.exclude(footer=False)

@register.assignment_tag
def footer_text():
    return MainFooterText.objects.all()[0]
