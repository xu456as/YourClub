# _*_ encoding:utf-8 _*_
import xadmin
from User.models import UserProfile, UserRegistry, EmailVerifyRecord

class UserRegistryAdmin(object):
    pass


class EmailVerifyRecordAdmin(object):
    pass


# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(UserRegistry, UserRegistryAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)