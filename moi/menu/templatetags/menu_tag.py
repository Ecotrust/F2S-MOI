from django import template
from django.template.loader import get_template
from menu.models import Menu
from home.models import HomePage

register = template.Library()

@register.simple_tag(takes_context=True)
def menus(context, kind='header', menu_type='navbar'):

    t = get_template("menu/tags/%s.html" % menu_type)

    footer = (kind == 'footer')
    menus = Menu.objects.filter(footer=footer)
    nav_title = HomePage.objects.all()[0].display_title     

    return t.render(template.Context({
        'menus': menus,
        'nav_title': nav_title,
        'request': context['request'],
}))