from django.db import models
from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.models import Image
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

import validators

class Data(models.Model):
    DATA_CHOICES = (
        ('pie', 'Pie Chart'),
        ('bar', 'Bar Chart'),
        ('link', 'Yes! Link'),
        ('map', 'District Map'),
        ('number', 'Big Number'),
    )

    data_viz_type = models.CharField(choices=DATA_CHOICES,
                                     max_length=10,
                                     null=True,
                                     default=None,
                                     verbose_name='Data Viz Type',
                                     help_text='Select the type of data vizulation for this Core Measure')
    source = models.TextField(blank=True,
                              null=True,
                              default="",
                              help_text='Source text for data visualization')
    year = models.CharField(blank=True,
                            null=True,
                            default="",
                            max_length=255,
                            help_text='Input the year/date range for the associated data visualization')
    data_values = models.TextField(blank=True,
                             null=True,
                             default="",
                             verbose_name='Data',
                             help_text='Enter your values here. If there is more than one value present, separate them by a semicolon')
    data_labels = models.CharField(blank=True,
                             null=True,
                             default="",
                             max_length=255,
                             verbose_name="Data Labels",
                             help_text='Enter your labels here. If there is more than one label present, separate them by a semicolon')

    content_panels = [
        FieldPanel('data_viz_type'),
        FieldPanel('source'),
        FieldPanel('year'),
        FieldPanel('data_values'),
        FieldPanel('data_labels'),
    ]

    def chart_data(request):
        viz_obj = request
        chart = viz_obj.data_viz_type
        ydata = viz_obj.data_values.split("; ")
        xdata = viz_obj.data_labels.split("; ")
        y_values = [ int(y) for y in ydata ]
        x_values = [ str(x) for x in xdata ]

        #check what type of chart
        if chart == 'pie':
            chartcontainer = "piechart_container%s" % (viz_obj.page_id)

            #if pie - it must add up to 100%
            if y_values and sum(y_values) < 100:
                remaining_val = (100 - sum(y_values))
                y_values.append(remaining_val)
        else:
            chart = 'multiBarHorizontal'
            chartcontainer = "barchart_container%s" % (viz_obj.page_id)

        #there must be a label for every value
        if x_values:
            while len(x_values) != len(y_values):
                x_values.append('')

        #create dict within list
        y_values = [ {'value':y} for y in y_values ]
        x_values = [ {'label':x} for x in x_values ]
        chartdata = y_values

        #labels will be updated to existing values
        #nvd3 takes a single list of label, val pairs
        for index, val in enumerate(chartdata):
            for indx, label in enumerate(x_values):
                if index == indx:
                    val.update(label)

        #return data object
        data = {
            'id': viz_obj.page_id,
            'charttype': str(chart),
            'chartdata': chartdata,
            'chartcontainer': chartcontainer,
            'source': str(viz_obj.source),
            'year': str(viz_obj.year),
        }

        return data

    def district_map_data(request):
        data_values = request.data_values.split("; ")
        district_ids = [ int(val) for val in data_values ]

        map_params = {
            'id': request.page_id,
            'data_values': district_ids,
            'year': request.year,
        }

        return map_params

    def big_number_data(request):
        number_params = request
        value = number_params.data_values
        sign = ''

        if value.startswith('$'):
            value = value[1:]
            sign = '$'

        big_num = int(value)
        number_params.data_values = "<span class='dollar-sign'>%s</span><span id='count-%s' class='count-up'></span>" % (sign, big_num)

        return number_params

    def link_data(request):
        if validators.url(request.data_values):
            request.data_values = str(request.data_values)
        else:
            request.data_values = '#'

        return request

    @property
    def data_object(self):
        if self.data_values.endswith(";"):
            self.data_values = self.data_values[:-1]

        if self.data_labels.endswith(";"):
            self.data_labels = self.data_labels[:-1]

        if self.data_viz_type == 'pie' or self.data_viz_type == 'bar':
            return self.chart_data()
        elif self.data_viz_type == 'map':
            return self.district_map_data()
        elif self.data_viz_type == 'number':
            return self.big_number_data()
        elif self.data_viz_type == 'link':
            return self.link_data()

    class Meta:
        abstract = True

