from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

class Data(models.Model):
    DATA_CHOICES = (
        ('pie', 'Pie Chart'),
        ('bar', 'Bar Chart'),
        ('link', 'Link'),
        ('list', 'List'),
        ('map', 'Map'),
        ('number', 'Big Number'),
    )

    data_viz_type = models.CharField(choices=DATA_CHOICES,
                                       max_length=1,
                                       null=True,
                                       default="",
                                       verbose_name='Data Viz Type',
                                       help_text='Select the type of data vizulation for this Core Measure')
    prime_label = models.TextField(blank=True, 
                                   null=True,
                                   default="", 
                                   verbose_name='Prime Label', 
                                   help_text='This will be primary label/text for the data visualization')
    source = models.TextField(blank=True, 
                              null=True,
                              default="", 
                              help_text='Source text for data visualization')
    year = models.CharField(blank=True,
                            null=True,
                            default="",
                            max_length=255,
                            help_text='Input the year/date range for the associated data visualization')
    data_values = models.CharField(blank=True, 
                             null=True,
                             default="", 
                             max_length=255,
                             verbose_name='Data', 
                             help_text='Enter your values here. If there is more than one value present, separate them by a semicolon')
    data_labels = models.CharField(blank=True, 
                             null=True,
                             default="", 
                             max_length=255,
                             verbose_name="Data Labels", 
                             help_text='Enter your labels here. If there is more than one label present, separate them by a semicolon')
    x_axis_label = models.CharField(blank=True, 
                             null=True,
                             default="", 
                             max_length=255,
                             verbose_name='X-Axis Label', 
                             help_text='Enter your x-axis label here')
    y_axis_label = models.CharField(blank=True, 
                             null=True,
                             default="", 
                             max_length=255,
                             verbose_name='Y-Axis Label', 
                             help_text='Enter your y-axis label here')


    content_panels = [
        FieldPanel('data_viz_type'),
        FieldPanel('prime_label'),
        FieldPanel('year'),
        FieldPanel('year'),
        FieldPanel('data_values'),
        FieldPanel('data_labels'),
        FieldPanel('x_axis_label'),
        FieldPanel('y_axis_label'),
    ]

    class Meta:
        abstract = True
