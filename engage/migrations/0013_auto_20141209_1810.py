# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0012_apiconfig'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apiconfig',
            name='id',
        ),
        migrations.AlterField(
            model_name='apiconfig',
            name='token',
            field=models.CharField(max_length=200, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
