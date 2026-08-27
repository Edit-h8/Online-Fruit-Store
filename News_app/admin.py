from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(news)
class new_admin(admin.ModelAdmin):
    list_display=["title" , "aother" , "created_date"]
    list_filter=["aother"]
    search_fields=["title" , "discribtion"]

@admin.register(tag)
class tag_admin(admin.ModelAdmin):
    pass