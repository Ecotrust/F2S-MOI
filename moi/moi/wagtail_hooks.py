from django.utils.html import format_html
from django.conf import settings

from wagtail.wagtailcore import hooks

@hooks.register('insert_editor_css')
def editor_css():
  return format_html('<link rel="stylesheet" type="text/x-scss" href="' \
  + settings.STATIC_URL \
  + 'css/assets/wagtail_overrides.scss">')