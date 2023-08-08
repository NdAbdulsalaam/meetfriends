from django.contrib import admin
from .models import Member

# Register your models here.

class MemeberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastnaame", "joined_date")
                   
admin.site.register(Member)