from django.urls import path

from products.views import create_product, list_products, create_costumer, costumer_list, costumerDeleteView, costumerUpdateView, create_location, location_list, location_update, locationDeleteView

urlpatterns = [
    path('create_product/', create_product),
    path('list_products/', list_products),
    
    path ('create_costumer/', create_costumer),
    path ('costumer_list/', costumer_list),
    path ('costumer_update/<int:pk>/', costumerUpdateView.as_view(), name='costumer_update'),
    path ('costumer_delete/<int:pk>/', costumerDeleteView.as_view(), name='costumer_delete'),
    
    path('create_location/', create_location, name='location_create'),
    path('location_list/', location_list, name= 'location_list'),
    path('location_update/<int:id>/', location_update, name='location_update'),
    path('location_delete/<int:pk>/', locationDeleteView.as_view(), name='location_delete'),
    ]
