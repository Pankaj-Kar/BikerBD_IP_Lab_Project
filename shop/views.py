from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    params = {'product' : products}

    return render(request, 'shop/shopping_list.html', params)
    
def contact(request):
    return render(request, 'shop/shopping_list.html')

def tracker(request):
    return render(request, 'shop/shopping_list.html')
    
def search(request):
    return render(request, 'shop/shopping_list.html')
    
def prodView(request, myid):
    product = Product.objects.filter(id=myid)
    
    return render(request, 'shop/prod_view.html', {'prod':product[0]})
    
def checkout(request):
    return render(request, 'shop/checkout.html')
    