from django.db import models

class products (models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.BooleanField()
    
    def __str__(self):
        return self.name