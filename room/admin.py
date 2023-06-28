from django.contrib import admin
from .models import GroupRoom, Message, Guest, NormalRoom

# Register your models here.
admin.site.register(GroupRoom)
admin.site.register(Message)
admin.site.register(Guest)
admin.site.register(NormalRoom)
