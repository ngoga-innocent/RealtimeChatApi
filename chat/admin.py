from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Room)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'room', 'message')
admin.site.register(Message,MessageAdmin)