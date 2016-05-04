from wagtail.wagtailimages.formats import Format, register_image_format, unregister_image_format

unregister_image_format('fullwidth')
register_image_format(Format('fullwidth', 'Full width', 'richtext-image full-width img-responsive', 'width-850'))

unregister_image_format('left')

unregister_image_format('right')

register_image_format(Format('center', 'Centered', 'richtext-image img-responsive center-block', 'original'))

register_image_format(Format('multiple', 'Multiple Images', 'richtext-image img-responsive multi', 'original'))

register_image_format(Format('admin', 'Admin Default', 'richtext-image img-responsive center-block', 'max-600x450'))
