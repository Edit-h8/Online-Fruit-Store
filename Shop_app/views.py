from django.shortcuts import render , redirect
from . models import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone
from django.core.paginator import Paginator
# Create your views here.


#                                                            INDEX  PAGE
def index_page(request):
    pruduction =product.objects.all()
    paginator = Paginator(pruduction , 3)
    page_number = request.GET.get("page")

    pruduc_pagi = paginator.get_page(page_number)

    name_product = product.objects.values("name").distinct()

    name_product =product.objects.values("name").distinct()
    contact = {
        "name_product" : name_product,
        "pruduc_pagi" : pruduc_pagi,
        }
    return render(request , "Shop/shop.html" , contact)


#                                                    +       ADD CART PAGE
@login_required
def add_cart(request , pr_id):


    Product = get_object_or_404(product , id = pr_id)

    user = request.user

    cart , cart_created = Cart.objects.get_or_create( user = user)

    cart_item , cart_item_created = Cart_Item.objects.get_or_create(
        cart = cart ,
        produc = Product
    )

    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect("shop:cart")


#                                                      -     REMOVE CART PAGE

def remove_cart(request , product_id):
    print(f"ID = {product_id}")
    cart = Cart.objects.get(user = request.user)

    cart_item = Cart_Item.objects.get(
        cart=cart,
        produc_id = product_id
    )

    cart_item.delete()

    return redirect('shop:cart')


#                                                              CART PAGE
@login_required
def cart_page(request):

    cart = Cart.objects.get(user = request.user)

    cart_items = Cart_Item.objects.filter(cart = cart)

    subtotal = 0
    shiping = 45   

    for item in cart_items:
        subtotal += item.produc.price * item.quantity

    total = subtotal + shiping

    contact = {
        "cart_item":cart_items,
        "subtotal" : subtotal,
        "shiping" : shiping,
        "total" : total
        }
    return render(request , "Shop/cart.html" , contact)


#                                                               CHECKOUT PAGE
@login_required
def checkout_page(request):

    user = request.user

    cart = Cart.objects.get(user = user)

    cart_item = Cart_Item.objects.filter(cart = cart)

    subtotal = 0
    shiping = 45   

    for item in cart_item:
        subtotal += item.produc.price * item.quantity

    total = subtotal + shiping

    contact = {
        "cart_item":cart_item,
        "subtotal" : subtotal,
        "shiping" : shiping,
        "total" : total
        }
    
    return render(request , "Shop/checkout.html" , contact)






#                                                                  SINGLE PAGE
def single_page(request):
    return render(request , "Shop/single-Product.html")    



#                                                                     ORDER PAGE
@login_required
def order_page(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-id")

    return render(
        request,
        "Shop/order.html",
        {
            "orders": orders
        }
    )   



#                                                                     ADD ORDER +
@login_required
def add_order(request ):
    cart , created_cart = Cart.objects.get_or_create(user = request.user)
    
    cart_item = Cart_Item.objects.filter(cart = cart)

    total = 0

    for item in cart_item:
        total += (item.produc.price * item.quantity)


    order = Order.objects.filter(
        user=request.user,
        status="pending"
    ).first()


    if order:

        if timezone.now() >= order.expires_at:

            order.status = "expired"
            order.save(update_fields=["status"])

            messages.add_message(request , messages.ERROR , "your time exprice")
            order = None



    if not order:

        order = Order.objects.create(
            user=request.user,
            total_price=total,
            status="pending",
            expires_at=timezone.now() + timedelta(minutes=9)
        )

        for item in cart_item:
            Order_item.objects.create(
                order=order,
                Product=item.produc,
                quantity=item.quantity,
                price=item.produc.price
            )

        cart_item.delete()




    return redirect("shop:payment" , order_id=order.id )


#                                                                    PAYMENT PAGE
@login_required
def payment_page(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if request.method == "POST":
        
        pay = request.POST.get("pay")
        cancel = request.POST.get("cancel")
    
        if pay:
            
            order.status = "paid"
            order.save()
            messages.success(request , "Successfuly Paid")
            
            return redirect("shop:order")

        elif cancel:
           
            order.status = "cancelled"
            order.save()
            messages.success(request , "Successfuly cancel")
  
            return redirect("shop:order")
    return render(
        request,
        "Shop/payment.html",
        {"order": order}
    )
    
