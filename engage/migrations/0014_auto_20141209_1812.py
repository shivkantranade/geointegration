# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0013_auto_20141209_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiconfig',
            options={'verbose_name': 'API Configuration'},
        ),
    ]
