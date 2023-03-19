from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from usermodify.models import UserModify

class UserInline(admin.StackedInline):
    model = UserModify
    can_delete = False
    verbose_name_plural = 'UserModify'

class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)
    list_display = ('username','first_name','last_name','email','getUserPhone')
    def getUserPhone(self, object):
        return object.usermodify.phone
    
    getUserPhone.short_description = "phone"
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)