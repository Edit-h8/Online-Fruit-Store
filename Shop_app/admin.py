from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(product)
class admin_production(admin.ModelAdmin):
     search_fields = ["name" , ]
     list_display = ("name","price", "stock",)

@admin.register(Cart_Item)
class admin_Cart_item(admin.ModelAdmin):
     list_display = ("cart","produc" , "quantity")

@admin.register(Cart)
class admin_Cart(admin.ModelAdmin):
     list_display = ("user",)


@admin.register(Order)
class admin_Order(admin.ModelAdmin):
     list_display = ("user" , "status" , "created_data")


@admin.register(Order_item)
class admin_Order_item(admin.ModelAdmin):
     list_display = ("order","Product","price")

@admin.register(Payment)
class admin_Payment(admin.ModelAdmin):
     list_display = ("order","status","created_data" , "amount")