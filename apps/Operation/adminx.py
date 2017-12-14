# _*_ encoding:utf-8 _*_
import xadmin
from Operation.models import Message, ParticipatedActivity, MarkedActivity, MarkedComment
from xadmin import views


class MessageAdmin(object):
    pass


class ParticipatedActivityAdmin(object):
    pass


class MarkedActivityAdmin(object):
    pass


class MarkedCommentAdmin(object):
    pass

xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(ParticipatedActivity, ParticipatedActivityAdmin)
xadmin.site.register(MarkedActivity, MarkedActivityAdmin)
xadmin.site.register(MarkedComment, MarkedCommentAdmin)


class CommonSettings(object):
    site_title = u"O2O社交娱乐后台管理系统"
    site_footer = u"2017 - 2018 XXX Organization, All Rights Reserved"


xadmin.site.register(views.CommAdminView, CommonSettings)


