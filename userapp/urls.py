from django.urls import path
from . import views

urlpatterns = [
    path('user', views.user, name='user'),
    path('cardcategory', views.cardcategory, name='cardcategory'),
    path('cardproduct/<str:category>', views.cardproduct, name='cardproduct'),
    path('single/<int:id>', views.single, name='single'),
    path('contact', views.contact, name='contact'),
    path('contact_page', views.contact_page, name='contact_page'),
    path('registration', views.registration, name='registration'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('login', views.login, name='login'),
    path('userlogout', views.userlogout, name='userlogout'),
    path('publicdata', views.publicdata, name='publicdata'),
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('cart_data/<int:id>', views.cart_data, name='cart_data'),
    path('checkout', views.checkout, name='checkout'),
    path('deleted/<int:id>', views.deleted, name='deleted'),
    path('checkoutdata', views.checkoutdata, name='checkoutdata'),
    path('success', views.success, name='success'),
    path('about', views.about, name='about')
]