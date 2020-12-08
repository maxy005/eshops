from django.db import models


class customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=15)


    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return customer.objects.get(email=email)
        except:
            return False



    def isexist(self):
        if customer.objects.filter(email=self.email):
            return True
        else:
            return False

    def __str__(self):
       return self.first_name