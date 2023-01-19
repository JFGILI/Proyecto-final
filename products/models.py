from django.db import models

class products (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class costumer (models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    phone_number= models.IntegerField()
    
    def __str__(self):
        return self.phone_number

class Location (models.Model):
    name = models.CharField(max_length=20, )
    phone_number= models.IntegerField()
    
    def __str__(self):
        return self.name