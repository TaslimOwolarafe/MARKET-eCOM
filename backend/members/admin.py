from django.contrib import admin
from .models import Customer, Company, Cart, CartItem, ShippingAddress, Product, Category
# Register your models here.

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ShippingAddress)
admin.site.register(Product)
admin.site.register(Category)

