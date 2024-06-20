from django.db import models

class Customer(models.Model):
     customer_code = models.CharField(max_length=10, unique=True)
     customer_name = models.TextField(max_length = 255)
     customer_phonenumber = models.CharField(max_length = 13)
     customer_email = models.EmailField()
     
     def __str__(self):
        return self.customer_name
