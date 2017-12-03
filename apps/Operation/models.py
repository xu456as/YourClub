from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.
from User.models import UserProfile


class Message(models.Model):
    type = models.CharField(verbose_name=u"消息类型", choices=(('system', u"系统消息"), ('user', u"用户消息")), max_length=30)
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
