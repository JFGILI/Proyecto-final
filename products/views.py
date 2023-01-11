from django.shortcuts import render
from django.http import HttpResponse

from products.models import products

def create_product(request):
    new_product = products.objects.create(name="bebida", price=400, stock=True)
    return HttpResponse('Se creo el producto')

def list_products(request):
    all_products=products.objects.all()
    context={'products':all_products}
    return render(request, 'products/list_products.html', context=context)


