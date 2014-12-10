# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0006_geofence_update_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geofence',
            old_name='create_user',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='geofence',
            old_name='update_user',
            new_name='updated_by',
        ),
    ]
