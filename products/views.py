from django.shortcuts import render
from django.http import HttpResponse
from products.forms import LocationForm

from products.models import products, costumer, Location

def create_product(request):
    if request.method == 'GET':
        return render (request, 'products/create_product.html', context={})
    
    elif request.method == 'POST':
        products.objects.create(name=request.POST['name'], price=request.POST['price'])
        return render (request, 'products/create_product.html', context={})
        
def list_products(request):
    if 'search' in request.GET:
        search =request.GET['search']
        all_products= products.objects.filter(name__icontains=search)
        
    else:
        all_products= products.objects.all()
    
    context={'products': all_products}
    return render(request, 'products/list_products.html', context=context)

def create_costumer(request):
    if request.method == 'GET':
        return render (request, 'costumer/create_costumer.html', context={})
    
    elif request.method == 'POST':
        costumer.objects.create(name=request.POST['name'], email=request.POST['email'], phone_number=request.POST['phone'])
        return render (request, 'costumer/create_costumer.html', context={})

def costumer_list(request):
    all_costumer = costumer.objects.all()
    context = {'costumer': all_costumer}
    return render(request, 'costumer/costumer_list.html', context=context)

def create_location(request):

    if request.method == 'GET':
        context={
            'form':LocationForm()
        }
        return render (request, 'location/create_location.html', context=context)
    
    elif request.method == 'POST':
        Location.objects.create(name=request.POST['name'], phone_number=request.POST['phone_number'])
        return render (request, 'location/create_location.html', context={})
        
def location_list(request):
    all_location= Location.objects.all()
    context = {'location':all_location}
    return render (request, 'location/location_list.html', context=context)