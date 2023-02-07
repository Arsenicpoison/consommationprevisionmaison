from django.db import models
from app.models import Product


class Acheter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.CharField(max_length=100)
    date= models.DateField()    
    unit_price = models.CharField(max_length=100)
    total_price = models.IntegerField(null='True')

    def __str__(self) -> str:
        return self.quantite + " " +str(self.product)