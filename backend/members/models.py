from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
# from django.db.models.signals import post_delete
# from django.dispatch import receiver

# Create your models here.


class Company(models.Model):
    owner = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=300, null=True)
    brand = models.ImageField(upload_to="images/companies/", null=True, blank=True)
    account_no = models.PositiveIntegerField(validators=[MaxLengthValidator(10)],default=1131164190)
    bank_name = models.CharField(max_length=225, default="Polaris Bank Ltd.")
    # customer_orders = models.ManyToManyField(Cart)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=25)
    display_picture = models.ImageField(null=True, blank=True, upload_to='images/customers/')
    bio = models.TextField(max_length=225, null=True, blank=True)

    def __str__(self):
        return f"customer {self.display_name} of {self.user}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="", null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{str(self.id)} for {self.company}"
    
    @property
    def get_cart_total(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.get_total for item in cartitems])
        return total
    
    @property
    def get_cart_items(self):
        cartitems = self.cartitem_set.all()
        total = sum([item.quantity for item in cartitems])
        return total




class Product(models.Model):
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=225, null=True)
    image = models.ImageField(upload_to="images/products/")
    description = models.TextField(max_length=225, blank=True)
    category = models.CharField(max_length=225, blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    # discount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.title




class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.title} on {self.cart}"

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default="", null=True, blank=True)
    order = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=225, null=True)
    state = models.CharField(max_length=225, null=True)
    zipcode = models.CharField(max_length=225, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    receipt = models.ImageField(upload_to="images/companies/receipts", null=True, blank=True)

    def __str__(self):
        return f"{self.customer}'s {self.order} on {self.company}"


class Category(models.Model):
    name = models.CharField(max_length=225)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


