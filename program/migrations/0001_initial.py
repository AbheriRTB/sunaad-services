# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1024)),
                ('event_date', models.DateField()),
                ('place', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('event_start', models.TimeField()),
                ('event_end', models.TimeField()),
                ('duration', models.FloatField()),
                ('location_address', models.CharField(max_length=512)),
                ('location_mapcoords', models.CharField(max_length=100)),
                ('location_parking', models.CharField(max_length=100)),
                ('location_eataries', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=b'path/', verbose_name=b'Label')),
            ],
        ),
    ]
