# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('engage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geofence',
            name='geofencecircle',
        ),
        migrations.DeleteModel(
            name='GeofenceCircle',
        ),
        migrations.AddField(
            model_name='geofence',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geofence',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='geofence',
            name='radius',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
