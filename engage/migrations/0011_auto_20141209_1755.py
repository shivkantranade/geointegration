# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0010_beacon_geofence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beacon',
            name='id',
        ),
        migrations.AlterField(
            model_name='beacon',
            name='factory_id',
            field=models.CharField(max_length=10, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
