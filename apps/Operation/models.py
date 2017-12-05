# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

from Activity.models import Activity
from User.models import UserProfile


# Create your models here.
class Message(models.Model):
    type = models.CharField(verbose_name=u"消息类型",
                            choices=(('system', u"系统消息"), ('user', u"用户消息")), max_length=30)
    content = models.CharField(verbose_name=u"消息内容", max_length=400)
    source = models.CharField(max_length=100, verbose_name=u"消息源")
    target = models.ForeignKey(UserProfile, verbose_name=u"消息目标", null=True, blank=True)
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    class Meta:
        verbose_name = u"推送消息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}给{1}的消息".format(self.source, self.target)


class ParticipatedActivity(models.Model):
    activity = models.ForeignKey(Activity, verbose_name=u"活动")
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"参与的活动"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}参与的{1}".format(self.user, self.activity)


class MarkedActivity(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    activity = models.ForeignKey(Activity, verbose_name=u"活动")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收藏的活动"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}收藏的{1}".format(self.user, self.activity)


class MarkedComment(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    comment = models.ForeignKey(Activity, verbose_name=u"说说")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"收藏的说说"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}收藏的{1}".format(self.user, self.comment)








