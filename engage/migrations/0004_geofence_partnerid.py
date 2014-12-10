# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('engage', '0003_auto_20141208_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='geofence',
            name='partnerid',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
