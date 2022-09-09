from distutils.command.upload import upload
from email.mime import image
from itertools import product
from django.db import models
from django.contrib.auth.models import User
from members.models import Customer
from members.models import Product

from members.models import Company
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    image = models.ImageField(upload_to='images/posts/' ,null=True, blank=True)
    post_time = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.content[:15]} | {self.author}'


class Annoncement(models.Model):
    author = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='admin')
    body = models.TextField(max_length=300)
    product = models.ForeignKey(Product, null=True, blank=True, related_name='attachment', on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True, upload_to='images/announcements/')