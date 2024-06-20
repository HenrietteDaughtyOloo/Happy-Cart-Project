from django.shortcuts import render
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
import africastalking
from django.conf import settings

# Create your views here.
africastalking.initialize(username='sandbox', api_key=settings.AFRICAS_TALKING_API_KEY)
sms = africastalking.SMS

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        send_sms_alert(order.customer.customer_name, order.customer.customer_phonenumber)


def send_sms_alert(customer_name, customer_phone):
    try:
        response = sms.send(f"Hello {customer_name}, your order has been placed successfully!", [customer_phone])
        print(f"SMS sent successfully to {customer_phone}. Response: {response}")
        if 'SMSMessageData' in response and 'Recipients' in response['SMSMessageData']:
            for recipient in response['SMSMessageData']['Recipients']:
                if recipient['status'] != 'Success':
                    print(f"SMS delivery failed for {recipient['number']}. Status: {recipient['status']}, Cost: {recipient['cost']}")

    except Exception as e:
        print(f"Failed to send SMS to {customer_phone}. Error: {str(e)}")

