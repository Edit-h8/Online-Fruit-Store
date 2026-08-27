"""
URL configuration for Shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path , include
from .views import *

app_name = "shop"

urlpatterns = [
    path("" , index_page , name="index"),
    path("checkout/" , checkout_page , name="checkout"),
    path("single/" ,single_page , name="single"),    

    #cart
    path("cart/" , cart_page , name="cart"),
    path("cart/add/<int:pr_id>" , add_cart , name="add_cart"),
    path("cart/remove/<int:product_id>" , remove_cart , name="remove_cart"),

    #order
    path("order/" , order_page , name="order"),
    path("order/add" , add_order, name="add_order"),

    #payment
   path("payment/<int:order_id>", payment_page , name="payment"),
   
]
