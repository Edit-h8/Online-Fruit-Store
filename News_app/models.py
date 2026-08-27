from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class tag(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name

class news(models.Model):
    title = models.CharField(max_length=100)
    aother = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='news/' , default='news/default.jpg')
    tag= models.ManyToManyField(tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title