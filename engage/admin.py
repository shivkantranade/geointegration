from django.contrib import admin
from engage.models import Geofence, Beacon, APIConfig
import requests
import collections
import json


class APIConfigAdmin(admin.ModelAdmin):
    list_display = ('token', 'url', 'organization')

    list_filter = ['token', 'url', 'organization']

    search_fields = ['token', 'url', 'organization']


class GeofenceAdmin(admin.ModelAdmin):

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Define location:', {'fields': ['address', 'latitude', 'longitude', 'radius']}),
        (None, {'fields': ['pub_date']}),
    ]

    list_display = ('name', 'address', 'latitude', 'longitude', 'radius', 'pid', 'pub_date', 'created_by', 'updated_by')

    list_filter = ['pub_date', 'created_by', 'updated_by']

    search_fields = ['name', 'address', 'created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        if change:
            # User tried updating geofence
            print change

            # set api token, url for gimbal
            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # update existing geofence in gimbal
            locationpayload = collections.OrderedDict()
            locationpayload['latitude'] = obj.latitude
            locationpayload['longitude'] = obj.longitude

            geocirclepayload = collections.OrderedDict()
            geocirclepayload['radius'] = obj.radius
            geocirclepayload['location'] = locationpayload

            geoplaceattrib = collections.OrderedDict()
            geoplaceattrib['key1'] = 'value1'
            geoplaceattrib['key2'] = 'value2'

            geopayload = collections.OrderedDict()
            geopayload['name'] = obj.name
            geopayload['addressLineOne'] = obj.address
            geopayload['geoFenceCircle'] = geocirclepayload
            geopayload['placeattributes'] = geoplaceattrib

            geojson = json.dumps(geopayload)

            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "geofences/" + str(obj.partnerid)
            print geopayload
            print ''
            print geojson
            print posturl

            r = requests.put(posturl, data=geojson, headers=headers)
            print "UPDATED GEOFENCE"
            print r.status_code

            if r.status_code == 200:
                print r.json()
                geoid = r.json().get("id")
                print geoid

                obj.partnerid = int(geoid)
                obj.updated_by = request.user.username
                print request.user.username
                obj.save()

        else:
            # User tried creating a geofence
            print change

            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # create new geofence in gimbal
            locationpayload = collections.OrderedDict()
            locationpayload['latitude'] = obj.latitude
            locationpayload['longitude'] = obj.longitude

            geocirclepayload = collections.OrderedDict()
            geocirclepayload['radius'] = obj.radius
            geocirclepayload['location'] = locationpayload

            geoplaceattrib = collections.OrderedDict()
            geoplaceattrib['key1'] = 'value1'
            geoplaceattrib['key2'] = 'value2'

            geopayload = collections.OrderedDict()
            geopayload['name'] = obj.name
            geopayload['addressLineOne'] = obj.address
            geopayload['geoFenceCircle'] = geocirclepayload
            geopayload['placeattributes'] = geoplaceattrib

            geojson = json.dumps(geopayload)

            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "geofences"
            print geopayload
            print ''
            print geojson
            print posturl

            r = requests.post(posturl, data=geojson, headers=headers)
            print "CREATED GEOFENCE"
            print r.status_code

            if r.status_code == 200:
                print r.json()
                geoid = r.json().get("id")
                print geoid

                obj.partnerid = int(geoid)
                obj.created_by = request.user.username
                obj.save()

    def delete_model(self, request, obj):
        # set api token, url for gimbal
        tk = APIConfig.objects.all()
        token = "Token token=" + tk[0].token
        url = tk[0].url

        print "-----------"
        print token
        print url
        print "-----------"

        # delete existing geofence from gimbal
        headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
        posturl = url + "geofences/" + str(obj.partnerid)
        print posturl

        r = requests.delete(posturl, headers=headers)
        print "DELETED GEOFENCE"
        print r.status_code

        if r.status_code == 200:
            obj.delete()

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            # set api token, url for gimbal
            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # delete existing geofence from gimbal
            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "geofences/" + str(o.partnerid)
            print posturl

            r = requests.delete(posturl, headers=headers)
            print "DELETED GEOFENCE"
            print r.status_code

            if r.status_code == 200:
                o.delete()


class BeaconAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['factory_id']}),
        (None, {'fields': ['name']}),
        ('Define beacon location:', {'fields': ['latitude', 'longitude']}),
        (None, {'fields': ['pub_date']}),
    ]

    list_display = ('name', 'factory_id', 'latitude', 'longitude', 'pub_date', 'activated_by', 'updated_by')

    list_filter = ['pub_date', 'activated_by', 'updated_by']

    search_fields = ['name', 'factory_id', 'activated_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        if change:
            print change

            # set api token, url for gimbal
            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # update existing beacon in gimbal
            beaconpayload = collections.OrderedDict()
            beaconpayload['name'] = obj.name
            beaconpayload['latitude'] = obj.latitude
            beaconpayload['longitude'] = obj.longitude

            beaconjson = json.dumps(beaconpayload)

            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "beacons/" + obj.factory_id
            print beaconpayload
            print ''
            print beaconjson
            print posturl

            r = requests.put(posturl, data=beaconjson, headers=headers)
            print "UPDATED BEACON"
            print r.status_code

            if r.status_code == 200:
                print r.json()
                factory_id = r.json().get("factory_id")
                print factory_id

                print request.user.username
                obj.updated_by = request.user.username

                obj.save()

        else:
            print change

            # set api token, url for gimbal
            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # create new geofence in gimbal
            beaconpayload = collections.OrderedDict()
            beaconpayload['factory_id'] = obj.factory_id
            beaconpayload['name'] = obj.name
            beaconpayload['latitude'] = obj.latitude
            beaconpayload['longitude'] = obj.longitude

            beaconjson = json.dumps(beaconpayload)

            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "beacons"
            print beaconpayload
            print ''
            print beaconjson
            print posturl

            r = requests.post(posturl, data=beaconjson, headers=headers)
            print "ACTIVATED BEACON"
            print r.status_code

            if r.status_code == 200:
                print r.json()
                factory_id = r.json().get("factory_id")
                print factory_id

                obj.activated_by = request.user.username
                obj.save()

    def delete_model(self, request, obj):
        # set api token, url for gimbal
        tk = APIConfig.objects.all()
        token = "Token token=" + tk[0].token
        url = tk[0].url
        print "-----------"
        print token
        print url
        print "-----------"

        # delete existing geofence from gimbal
        headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
        posturl = url + "beacons/" + obj.factory_id
        print posturl

        r = requests.delete(posturl, headers=headers)
        print "DELETED BEACON"
        print r.status_code

        if r.status_code == 200:
            obj.delete()

    actions = ['delete_selected']

    def delete_selected(self, request, obj):
        for o in obj.all():
            # set api token, url for gimbal
            tk = APIConfig.objects.all()
            token = "Token token=" + tk[0].token
            url = tk[0].url
            print "-----------"
            print token
            print url
            print "-----------"

            # delete existing geofence from gimbal
            headers = {'content-type': 'application/json', 'AUTHORIZATION': token}
            posturl = url + "beacons/" + o.factory_id
            print posturl

            r = requests.delete(posturl, headers=headers)
            print "DELETED BEACON"
            print r.status_code

            if r.status_code == 200:
                o.delete()


admin.site.register(Geofence, GeofenceAdmin)

admin.site.register(Beacon, BeaconAdmin)

admin.site.register(APIConfig, APIConfigAdmin)
