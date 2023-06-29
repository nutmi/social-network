from django.contrib import admin
from .models import GroupRoom, MessageNormalRoom, Guest, NormalRoom

# Register your models here.
admin.site.register(GroupRoom)
admin.site.register(MessageNormalRoom)
admin.site.register(Guest)
admin.site.register(NormalRoom)
