from django.db import models
from app.models import Category 

class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  product_name = models.CharField(max_length=30)

 


  def __str__(self) -> str:
      return self.product_name +" " +str(self.category)
  class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['product_name'],
                name = 'unique_product'
            )
        ]