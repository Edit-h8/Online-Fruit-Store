from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Contact)
class contact_admin(admin.ModelAdmin):
    list_display=["name" , "subject" , "created_date"]