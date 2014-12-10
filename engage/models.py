from __future__ import unicode_literals
from django.db import models

class APIConfig(models.Model):
    token = models.CharField(max_length=200, primary_key=True)
    url = models.URLField(max_length=200)
    organization = models.CharField(max_length=200)

    class Meta:
        verbose_name = "API Configuration"

class Geofence(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    radius = models.IntegerField(default=0)
    pub_date = models.DateTimeField('Date Published')
    partnerid = models.IntegerField(default=-1)
    created_by = models.CharField(max_length=200, default='')
    updated_by = models.CharField(max_length=200, default='')

    def pid(self):
        if self.partnerid == -1:
            return ''
        else:
            return str(self.partnerid)

    pid.short_description = 'Partner ID'

    def __str__(self):
        return self.name


class Beacon(models.Model):
    factory_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    pub_date = models.DateTimeField('Date Activated')
    activated_by = models.CharField(max_length=200, default='')
    updated_by = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name