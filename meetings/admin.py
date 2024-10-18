from django.contrib import admin

# Register your models here.
from meetings.models import Meeting, Room
admin.site.register(Meeting)
admin.site.register(Room)
