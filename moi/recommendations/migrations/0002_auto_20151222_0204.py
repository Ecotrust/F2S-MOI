# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0004_set_unique_on_path_and_site'),
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
        ('wagtailforms', '0002_add_verbose_names'),
        ('recommendations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendations',
            name='page_ptr',
        ),
        migrations.AlterModelOptions(
            name='recommendation',
            options={'verbose_name': 'Recommendation'},
        ),
        migrations.AddField(
            model_name='recommendation',
            name='page_type',
            field=models.CharField(default=b'Recommendation', max_length=255),
        ),
        migrations.DeleteModel(
            name='Recommendations',
        ),
    ]
