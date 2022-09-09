from cProfile import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from requests import get, request
from .models import Company, Customer, Product, CartItem, Cart, ShippingAddress
from .forms import EditUserForm, PasswordChangingForm, CreateProductForm, EditCompanyForm, EditCustomerForm, EditProductForm, SignUpForm, CompanyProfileForm, ShippingAddressUpdateForm, UserRegisterForm, CustomerProfileForm, CartItemUpdateForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
# def home(request):
#     return render(request, 'users/home.html')


class CreateCustomerProfileView(CreateView):
    model = Customer
    form_class = CustomerProfileForm
    template_name = 'customer/create_customer.html'
    fields = "__all__"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class CreateCompanyProfileView(CreateView):
    model = Company
    form_class = CompanyProfileForm
    template_name = 'companies/create_company.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')


class HomeView(ListView):
    model = Product
    template_name = 'users/home.html'

class CartItemsView(ListView):
    model = CartItem
    template_name = 'customer/cart_items.html'

    def get_context_data(self, *args, **kwargs):
        cart = CartItem.objects.filter(cart=self.kwargs['pk'])
        pk = cart.first().cart.id
        customer_id = cart.first().cart.customer.id
        # print(pk)
        context = super().get_context_data(*args, **kwargs)
        context['cart'] = cart
        context['id'] = pk
        context['customer_id'] = customer_id
        
        total = 0
        items = 0
        for item in cart:
            if item is not None:
                total+= (item.product.price*item.quantity)
                items+= (item.quantity)
        context['total'] = total
        context['items'] = items
        return context

    

# class CartListView(ListView):
#     model = Cart
#     template_name = 'customer/cart_list.html'

#     def get_queryset(self):

#         return super().get_queryset()

# def cart(request):
#     return render(request, 'customer/cart.html')

def ShippingCreateView(request):
    cart = get_object_or_404(Cart, id=request.POST.get('cart_id'))
    # customer = request.user.customer
    name = cart.customer.display_name
    email = cart.customer.user.email
    customer = cart.customer
    company = cart.company
    check = ShippingAddress.objects.get_or_create(customer=customer, company=company, order=cart, name=name, email=email)
    # print(check)
    return HttpResponseRedirect(reverse('shipping', args=[str(check[0].id), check[0].customer]))

class ShippingUpdateView(UpdateView):
    model = ShippingAddress
    template_name = 'customer/shipping.html'
    form_class = ShippingAddressUpdateForm

def CreateCartItem(request):
    product = get_object_or_404(Product, id=request.POST.get('product_id'))
    # product = Product.objects.get(id=request.POST.get("product_id"))
    print(product)
    cart = Cart.objects.get_or_create(customer=request.user.customer, company=product.owner)
    AddItem = CartItem.objects.get_or_create(product=product, cart=cart[0])
    # CartItem.objects.filter(pk=product.id).update(quantity=1)
    # return HttpResponseRedirect(reverse('cart-items', args=[str(AddItem[0].cart.id)]))
    return HttpResponseRedirect(reverse('cart-item-update', args=[str(AddItem[0].id)]))


class CartItemUpdateView(UpdateView):
    model = CartItem
    form_class = CartItemUpdateForm
    template_name = "customer/update_cart_item.html"


    def get_success_url(self, **kwargs):
        item = get_object_or_404(CartItem, id=self.kwargs['pk'])
        cart_id = item.cart.id
        return reverse_lazy('cart-items', args=[str(cart_id)])
    

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = "customer/cart_item_delete.html"

    def get_success_url(self, *args, **kwargs):
        item = get_object_or_404(CartItem, id=self.kwargs['pk'])
        cart_id = item.cart.id
        return reverse_lazy('cart-items', args=[str(cart_id)])
    # success_url = reverse_lazy('cart-list')


class CompanyPageView(DetailView):
    model = Company
    template_name = "companies/company_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_user = get_object_or_404(Company, id=self.kwargs['pk'])
        company_products = Product.objects.filter(owner=page_user)
        context["page_user"] = page_user
        context['company_product'] = company_products

        return context

class CustomerPageView(DetailView):
    model = Customer
    template_name = 'customer/customer_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Customer, id=self.kwargs['pk'])
        customer_carts = Cart.objects.filter(customer=self.kwargs['pk'])
        # pk = customer_carts.first().cart.id
        pk = customer_carts[0].id
        # print(pk)
        # context = super().get_context_data(*args, **kwargs)
        context['customer_carts'] = customer_carts
        context['id'] = pk
        context['page_user'] = page_user

        return context


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')


class CreateProductView(CreateView):
    model = Product
    form_class = CreateProductForm
    template_name = "companies/create_product.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user.company
        return super().form_valid(form)


    def get_success_url(self, *args, **kwargs):

        return reverse_lazy('company', args=[str(self.object.owner.id)])
    
class ProductEditView(UpdateView):
    form_class = EditProductForm
    model = Product
    template_name = 'companies/edit_product.html'

    def get_success_url(self, *args, **kwargs):

        return reverse_lazy('company', args=[str(self.object.owner.id)])


class CompanyEditView(UpdateView):
    form_class = EditCompanyForm
    model = Company
    template_name = "companies/edit_company.html"

    def get_success_url(self, *args, **kwargs):

        return reverse_lazy('company', args=[str(self.object.id)])

class EditCustomerView(UpdateView):
    form_class = EditCustomerForm
    model = Customer
    template_name = "customer/edit_customer.html"

    def get_success_url(self, *args, **kwargs):

        return reverse_lazy('customer', args=[str(self.object.id), self.object.display_name])


class PasswordChangingView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('password-success')


class UserEditView(UpdateView):
    form_class = EditUserForm
    template_name = 'users/change_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def password_success(request):
    return render(request, 'users/password_success.html', context={})




# def checkout(request, pk):
#     return render(request, 'customer/checkout.html')