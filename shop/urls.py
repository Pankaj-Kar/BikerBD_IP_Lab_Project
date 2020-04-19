from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='shop-home'),
    path('contact/', views.contact, name='contactus'),
    path('tracker/', views.tracker, name='trackstatus'),
    path('search/', views.search, name='search'),
    path('products/<int:myid>/', views.prodView, name='products'),
    path('checkout/', views.checkout, name='checkout'),

]