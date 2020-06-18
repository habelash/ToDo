from django.contrib import admin
from .models import timetable

# Register your models here.

admin.site.site_header = 'Todo'


class table(admin.ModelAdmin):
    list_display = ('title', 'discription', 'deadline', 'status')


admin.site.register(timetable, table)
