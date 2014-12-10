# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0005_geofence_create_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='geofence',
            name='update_user',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
