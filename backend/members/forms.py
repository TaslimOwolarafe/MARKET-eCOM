from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import CartItem, Company, Customer, Product, ShippingAddress
# from django.core.validators import MaxLengthValidator


class ShippingAddressUpdateForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ('name', 'email', 'order',
        'address', 'city', 'state', 
        'zipcode')

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'customer'}),
            'email' : forms.TextInput(attrs={'class':'form-control', }),
            'order' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'order'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'address'}),
            'city' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'city'}),
            'state' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'state'}),
            'zipcode' : forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'zipcode'}),
            # 'date_added' : forms.DateInput(attrs={'class':'form-control',}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('display_name', 'display_picture', 'bio')

        widgets = {
            'display_name': forms.TextInput(attrs={'class':'form-control'}),
            # 'display_picture': forms.ImageField(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'brand', 'account_no', 'bank_name')

        widgets = {
            # 'owner': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'bank_name' : forms.TextInput(attrs={'class':'form-control'}),
            'account_no' : forms.NumberInput(attrs={'class':'form-control', 'style':'-webkit-appearance: none; margin: 0;'}),

            # 'brand': forms.ImageField,
            
        }

class CartItemUpdateForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ('quantity',)

        widgets = {
            'quantity': forms.NumberInput(attrs={'class':'form-control'})
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'image', 'description', 'price')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'image': forms.ImageField(),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'style':'-webkit-appearance: none; margin: 0;'}),
        }

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'image', 'description', 'price')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'image': forms.ImageField(),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control', 'style':'-webkit-appearance: none; margin: 0;'}),
        }

class EditCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'address', 'brand', 'account_no', 'bank_name')

        widgets = {
            # 'owner': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'bank_name' : forms.TextInput(attrs={'class':'form-control'}),
            'account_no' : forms.NumberInput(attrs={'class':'form-control', 'style':'-webkit-appearance: none; margin: 0;'}),

            # 'brand': forms.ImageField,
            
        }

class EditCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('display_name', 'display_picture', 'bio')

        widgets = {
            'display_name': forms.TextInput(attrs={'class':'form-control'}),
            # 'display_picture': forms.ImageField(attrs={'class':'form-control'}),
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=70, widget= forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=70, widget= forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class EditUserForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control'}))
    # password = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control', 'type': 'hidden'}))
    last_login = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control', 'type':'hidden'}))
    is_superuser = forms.CharField(max_length=70, widget= forms.CheckboxInput(attrs={'class':'form-check', 'type':'hidden'}))
    is_staff = forms.CharField(max_length=70, widget= forms.CheckboxInput(attrs={'class':'form-check','type':'hidden' }))
    is_active = forms.CharField(max_length=70, widget= forms.CheckboxInput(attrs={'class':'form-check', 'type':'hidden'}))
    date_joined = forms.CharField(max_length=70, widget= forms.TextInput(attrs={'class':'form-control', 'type':'hidden'})) 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')
