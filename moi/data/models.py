from django.db import models
from django.shortcuts import render

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
                                       max_length=10,
                                       null=True,
                                       default=None,
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
        FieldPanel('source'),
        FieldPanel('year'),
        FieldPanel('data_values'),
        FieldPanel('data_labels'),
        FieldPanel('x_axis_label'),
        FieldPanel('y_axis_label'),
    ]

    def chart(request):
        viz_obj = request
        chart = viz_obj.data_viz_type
        xdata = viz_obj.data_values.split("; ")
        ydata = viz_obj.data_labels.split("; ")

        if chart == 'pie':
            charttype = "pieChart"
            chartcontainer = "piechart_container"
            x_values = [ int(x) for x in xdata ]
            y_values = ydata
        else:
            charttype = "discreteBarChart"
            chartcontainer = "discretebarchart_container"
            x_values = values
            y_values = [ int(y) for y in ydata ]

        chartdata = {'x': x_values, 'y': y_values}

        data = {
            'charttype': charttype,
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'extra': {
                'x_is_date': False,
                'x_axis_format': '',
                'tag_script_js': True,
                'jquery_on_ready': False,
            }
        }

        return data

    @property
    def data_object(self):
        if self.data_viz_type == 'pie' or self.data_viz_type == 'bar':
            return self.chart()

    class Meta:
        abstract = True

