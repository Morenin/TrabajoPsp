from django.contrib import admin
from nucleo.user.models import User
from nucleo.user.forms import UserForm
# Register your models here.



class UserAdmin(admin.ModelAdmin):
    form = UserForm
    ordering=['first_name']
    list_per_page=2


admin.site.register(User,UserAdmin)