# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('engage', '0002_auto_20141208_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('factory_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Activated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='geofence',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'Date Published'),
            preserve_default=True,
        ),
    ]
