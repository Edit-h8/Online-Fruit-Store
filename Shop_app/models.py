from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your models here.

class product(models.Model):
    name= models.CharField(max_length=225)
    price = models.IntegerField()
    image = models.ImageField(upload_to="shop/")
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

    
    

class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    produc = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



STATUS_CHOISES = [
    ("pending", "Pending ..."),
    ("paid", "Paid =]"),
    ("shipped", "Shipped"),
    ("expride", "Expride"),
    ("cancelled", "Cancelled =("),
]

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    status = models.CharField(max_length=50 , choices=STATUS_CHOISES , default="pending")
    total_price = models.IntegerField(null=True)
    created_data = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )


    def __str__(self):
        return str(self.user)


class Order_item(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    Product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()




class Payment(models.Model):
    order = models.OneToOneField(Order ,on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.CharField(max_length=50 , choices=STATUS_CHOISES , default="pending")
    transaction_id = models.CharField(max_length=100 , blank=True , null=True)
    created_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)