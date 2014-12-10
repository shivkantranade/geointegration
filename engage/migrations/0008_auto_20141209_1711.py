# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0007_auto_20141209_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='beacon',
            name='activated_by',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beacon',
            name='beacon_partner_id',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beacon',
            name='updated_by',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
