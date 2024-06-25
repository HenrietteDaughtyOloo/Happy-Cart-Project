import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
from .models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        client_id = settings.CLIENT_ID
        client_secret = settings.CLIENT_SECRET


        self.user = User.objects.create_user(username='Adalab', password='Lab@5708')


        response = self.client.post('/o/token/', {
            'grant_type': 'password',
            'username': 'Adalab',
            'password': 'Lab@5708',
            'client_id': client_id,
            'client_secret': client_secret
        })

        if response.status_code != status.HTTP_200_OK:
            print("Token request failed: ", response.content)
            print(f"Client ID: {client_id}")
            print(f"Client Secret: {client_secret}")

            raise Exception("Failed to obtain access token")

        response_data = response.json()
        self.access_token = response_data['access_token']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        self.customer_data = {
            'customer_code': '3001',
            'customer_name': 'Annestine',
            'customer_phonenumber': '+254791752690',
            'customer_email': 'anne@example.com'
        }

    def test_create_customer(self):
        response = self.client.post('/api/customers/', self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().customer_name, 'Annestine')

    def test_list_customers(self):
        Customer.objects.create(**self.customer_data)
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['customer_name'], 'Annestine')

    def test_retrieve_customer(self):
        customer = Customer.objects.create(**self.customer_data)
        response = self.client.get(f'/api/customers/{customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Annestine')

    def test_update_customer(self):
        customer = Customer.objects.create(**self.customer_data)
        updated_data = {
            'customer_code': 'CUST001',
            'customer_name': 'Liam Dickson',
            'customer_phonenumber': '+254700000000',
            'customer_email': 'liam@example.com'
        }
        response = self.client.put(f'/api/customers/{customer.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Customer.objects.get().customer_name, 'Liam Dickson')

    def test_delete_customer(self):
        customer = Customer.objects.create(**self.customer_data)
        response = self.client.delete(f'/api/customers/{customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)