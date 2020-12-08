from django.db import models
from .category import category

class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=100,default='')
    #category=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='upload/products/')


    @staticmethod
    def get_product_by_id_cart(ids):
        return product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_product():
        return product.objects.all()

    @staticmethod
    def get_all_product_by_id(category_id):
      if category_id:
        print(category_id,'here is the category id')
        return product.objects.filter(category=category_id)
      else:
        return product.get_all_product()

    def __str__(self):
        return self.name
