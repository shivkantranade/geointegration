# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0008_auto_20141209_1711'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Beacon',
        ),
        migrations.DeleteModel(
            name='Geofence',
        ),
    ]
