from django.urls import path
from . views import CartItemDeleteView, CartItemUpdateView, CompanyEditView, CompanyPageView, CreateCartItem, CreateCompanyProfileView, CreateCustomerProfileView, CreateProductView, CustomerPageView, EditCustomerView, HomeView, CartItemsView, PasswordChangingView, ProductEditView, ShippingUpdateView, ShippingCreateView, UserEditView, UserRegisterView, password_success


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("cart_items/<int:pk>/", CartItemsView.as_view(), name="cart-items"),
    # path("orders/", CartListView.as_view(), name="orders"),
    path("create_ship/", ShippingCreateView, name="create-ship"),
    path("shipping/<int:pk>/<str:name>/", ShippingUpdateView.as_view(), name="shipping"),
    path("create/customer_profile/<int:pk>/", CreateCustomerProfileView.as_view(), name="customer-profile"),
    path("register/<int:pk>/", UserRegisterView.as_view(), name="register"),
    path("create_company/<int:pk>/", CreateCompanyProfileView.as_view(), name="create-company"),
    path('create_cart_item/', CreateCartItem, name="create-cart-item"),
    path('cart_item_update/<int:pk>/', CartItemUpdateView.as_view(), name="cart-item-update"),
    path('cart_item_delete/<int:pk>/', CartItemDeleteView.as_view(), name="cart-item-delete"),
    path('company/<int:pk>/', CompanyPageView.as_view(), name='company'),
    path('customer/<int:pk>/<str:name>/', CustomerPageView.as_view(), name='customer'),
    path("register/", UserRegisterView.as_view(), name="register"),
    path('create_product/', CreateProductView.as_view(), name="create-product"),
    path('update_product/<int:pk>/', ProductEditView.as_view(), name="edit-product"),
    path('update_company/<int:pk>/', CompanyEditView.as_view(), name="edit-company"),
    path("update_customer/<int:pk>/", EditCustomerView.as_view(), name="edit-customer"),
    path("change-settings/", UserEditView.as_view(), name="edit-settings"),
    path("password/", PasswordChangingView.as_view(), name='change-password'),
    path("password-success/", password_success, name="password-success"),
]