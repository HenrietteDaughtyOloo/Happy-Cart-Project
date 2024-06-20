from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source='customer.customer_name', read_only=True)
    customer_phone = serializers.CharField(source='customer.customer_phonenumber', read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
