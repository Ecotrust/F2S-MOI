from django import template
from django.template.loader import get_template
from menu.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def menus(context, kind='header', menu_type='navbar'):

    t = get_template("menu/tags/%s.html" % menu_type)

    footer = (kind == 'footer')
    menus = Menu.objects.filter(footer=footer)

    return t.render(template.Context({
        'menus': menus,
        'request': context['request'],
}))