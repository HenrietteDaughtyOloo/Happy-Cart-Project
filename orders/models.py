from django.db import models

from customers.models import Customer

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    order_item = models.CharField(max_length=100)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_of_order = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" Order : {self.id} by customer {self.customer.customer_name}"