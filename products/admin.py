from django.contrib import admin

from products.models import products, costumer

@admin.register(products)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock', 'price')
    list_fields = ('name')

@admin.register(costumer)
class costumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    list_filter = ('name', 'email', 'phone_number')
    list_fields = ('name')