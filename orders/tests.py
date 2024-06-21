import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from customers.models import Customer
from .models import Order
from django.conf import settings

class OrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client_id = settings.CLIENT_ID
        self.client_secret = settings.CLIENT_SECRET

        self.user = User.objects.create_user(username='Adalab', password='Lab@5708')

        response = self.client.post('/o/token/', {
            'grant_type': 'password',
            'username': 'Adalab',
            'password': 'Lab@5708',
            'client_id': self.client_id,
            'client_secret': self.client_secret
        })

        if response.status_code != status.HTTP_200_OK:
            print("Token request failed: ", response.content)
            raise Exception("Failed to obtain access token")

        response_data = json.loads(response.content)
        self.access_token = response_data['access_token']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.customer = Customer.objects.create(
            customer_code='1001',
            customer_name='Hellena',
            customer_phonenumber='+254791752690',
            customer_email='hellena@gmail.com'
        )

        self.order_data = {
            'customer': self.customer.id,
            'order_item': 'Laptop',
            'order_amount': '1000.00'
        }

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().order_item, 'Laptop')

    def test_list_orders(self):
        Order.objects.create(**self.order_data)
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['order_item'], 'Laptop')

    def test_retrieve_order(self):
        order = Order.objects.create(**self.order_data)
        response = self.client.get(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['order_item'], 'Laptop')

    def test_update_order(self):
        order = Order.objects.create(**self.order_data)
        updated_data = {
            'customer': self.customer.id,
            'order_item': 'Smartphone',
            'order_amount': '1200.00'
        }
        response = self.client.put(f'/api/orders/{order.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.get().order_item, 'Smartphone')

    def test_delete_order(self):
        order = Order.objects.create(**self.order_data)
        response = self.client.delete(f'/api/orders/{order.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
