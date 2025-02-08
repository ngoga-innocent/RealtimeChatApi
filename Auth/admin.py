from django.contrib import admin
from .models import UserModel
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=['username', 'email', 'first_name', 'last_name']
admin.site.register(UserModel,UserAdmin)    