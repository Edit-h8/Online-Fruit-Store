from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name