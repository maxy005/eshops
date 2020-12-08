from django.contrib import admin
from .models.product import product
from .models.category import category
from .models.customer import customer

class adminproduct(admin.ModelAdmin):
    list_display = ['name','price']

class admincategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(product,adminproduct)
admin.site.register(category,admincategory)
admin.site.register(customer)

