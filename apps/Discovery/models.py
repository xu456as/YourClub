# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.
from User.models import UserProfile


class Comment(models.Model):
    id = models.AutoField(primary_key=True, unique=True) #自增主键
    user = models.ForeignKey(UserProfile, null=True, blank=True, default="", verbose_name=u"用户",)
    content = models.TextField(null = True, blank=True, verbose_name=u"文本内容")
    liked_number = models.IntegerField(default=0, verbose_name=u"点赞数")
    added_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    last_comment = models.IntegerField(default = -1, verbose_name=u"上一条评论的id") #指向上一条评论，如果为-1，则没有上一条评论

    class Meta:
        verbose_name = u"说说"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}的{1}的说说".format(self.user, self.id)


class Picture(models.Model):
    picture_url = models.ImageField(upload_to="comment/%Y/%m", max_length=100, verbose_name=u"评论的图片")
    comment = models.ForeignKey(Comment, verbose_name=u"评论")
    number = models.IntegerField(default = 0, verbose_name=u"号码") #标记该url为评论的第几张图片

    class Meta:
        verbose_name = u"评论的图片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u"{0}的第{1}张图片".format(self.comment.id, self.number)



