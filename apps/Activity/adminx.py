# _*_ encoding:utf-8 _*_
import xadmin
from Activity.models import CityDictionary, Activity


class CityDictionaryAdmin(object):
    list_display = ['name', 'desc']
    search_fields = ['name']


class ActivityAdmin(object):
    list_display = ['name', 'sponsor', 'restrict_number', 'city', 'start_time', 'end_time']
    search_fields = ['name']

xadmin.site.register(CityDictionary, CityDictionaryAdmin)
xadmin.site.register(Activity, ActivityAdmin)