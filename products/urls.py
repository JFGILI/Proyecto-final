from django.urls import path

from products.views import create_product, list_products, create_costumer, costumer_list, create_location, location_list, location_update

urlpatterns = [
    path('create_product/', create_product),
    path('list_products/', list_products),
    
    path ('create_costumer/', create_costumer),
    path ('costumer_list/', costumer_list),
    
    path('create_location/', create_location),
    path('location_list/', location_list),
    path('location_update/<int:id>/', location_update),
    ]
