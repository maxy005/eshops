from .product import models

class category(models.Model):
    name=models.CharField(max_length=100)

    @staticmethod
    def get_all_categorys():
       return category.objects.all()



    def __str__(self):
        return self.name
