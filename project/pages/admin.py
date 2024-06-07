
from django.contrib import admin
from .models import Admins,User,Department,UserhasDep,AdminsHasDep,search
# Register your models here.

admin.site.register(Admins),
admin.site.register(User),
admin.site.register(Department),
admin.site.register(UserhasDep),
admin.site.register(AdminsHasDep),
admin.site.register(search),
