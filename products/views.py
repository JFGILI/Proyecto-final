from django.shortcuts import render
from django.http import HttpResponse

from products.models import products, costumer, Location


def create_product(request):
    new_product= products.objects.create(name="postre", price=500, stock=True)
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
    new_costumer = costumer.objects.create(name="Francisco Gili", email=  'juanfrancisco54@hotmail.com',phone_number= 2612029373)
    return HttpResponse('Se creo un nuevo cliente')

def costumer_list(request):
    all_costumer = costumer.objects.all()
    context = {'costumer': all_costumer}
    return render(request, 'costumer/costumer_list.html', context=context)

def create_location(request):
    new_location = Location.objects.create(name="San Juan", phone_number= 263452489)
    return HttpResponse('Se creo un nuevo local')

def location_list(request):
    all_location= Location.objects.all()
    context = {'location':all_location}
    return render (request, 'location/location_list.html', context=context)