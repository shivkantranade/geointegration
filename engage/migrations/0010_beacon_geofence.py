# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engage', '0009_auto_20141209_1737'),
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
                ('activated_by', models.CharField(default=b'', max_length=200)),
                ('updated_by', models.CharField(default=b'', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Geofence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
                ('radius', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('partnerid', models.IntegerField(default=-1)),
                ('created_by', models.CharField(default=b'', max_length=200)),
                ('updated_by', models.CharField(default=b'', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
