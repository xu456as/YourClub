# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from User.models import UserProfile


# Create your models here.
class CityDictionary(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市")
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    added_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=20, default="", verbose_name=u"名字")
    description = models.CharField(max_length=100, default="", verbose_name=u"简述")
    sponsor = models.ForeignKey(UserProfile, verbose_name=u"发起人")
    image = models.ImageField(upload_to="Activity/%Y/%m", verbose_name=u"图片", max_length=100)
    restrict_number = models.IntegerField(default=500, verbose_name=u"人数限制")
    city = models.ForeignKey(CityDictionary, verbose_name=u"城市")
    address = models.CharField(max_length=100, verbose_name=u"详细地点")
    fee = models.DecimalField(default=0, decimal_places=2, max_digits=10, verbose_name=u"参与费用")
    start_time = models.DateTimeField(default=datetime.now, verbose_name=u"开始时间")
    end_time = models.DateTimeField(default=datetime.now, verbose_name=u"结束时间")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"活动"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

