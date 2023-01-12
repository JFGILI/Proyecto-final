from django.shortcuts import render
from django.http import HttpResponse

from products.models import products, costumer


def create_product(request):
    new_product= products.objects.create(name="bebida", price=400, stock=True)
    return HttpResponse('Se creo el producto')

def list_products(request):
    if 'search' in request.GET:
        search =request.GET['search']
        all_products= products.objects.filter(name__icontains=search)
        
    else:
        all_products= products.objects.all()
    
    context={'products': all_products}
    return render(request, 'products/list_products.html', context=context)

def create_costumer(request):
    new_costumer = costumer.objects.create(name="Daniela", email=  'dani@hotmail.com',phone_number= 2612029348)
    return HttpResponse('Se creo un nuevo cliente')

def costumer_list(request):
    all_costumer = costumer.objects.all()
    context = {'costumer': all_costumer}
    return render(request, 'costumer/costumer_list.html', context=context)

