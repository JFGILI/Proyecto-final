from django.db import models

class products (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products', verbose_name='Imagen')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    
class costumer (models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    phone_number= models.IntegerField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

class Location (models.Model):
    name = models.CharField(max_length=20, )
    phone_number= models.IntegerField()
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'
    
   