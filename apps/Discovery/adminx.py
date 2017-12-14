# _*_ encoding:utf-8 _*_
import xadmin
from Discovery.models import Comment, Picture


class CommentAdmin(object):
    pass


class PictureAdmin(object):
    pass


xadmin.site.register(Comment, CommentAdmin)
xadmin.site.register(Picture, PictureAdmin)