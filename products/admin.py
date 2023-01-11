from django.contrib import admin

from products.models import products



@admin.register(products)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    list_filter = ('stock', 'price')
    list_fields = ('name')
