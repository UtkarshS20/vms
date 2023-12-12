from django.test import TestCase

# Create your tests here.
# vendor_management_app/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Vendor, PurchaseOrder

class VendorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {'name': 'Test Vendor', 'contact_details': 'Contact Info', 'address': 'Vendor Address', 'vendor_code': 'V001'}

    def test_create_vendor(self):
        response = self.client.post(reverse('vendor-list-create'), self.vendor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 1)

    def test_get_vendors(self):
        Vendor.objects.create(name='Vendor1', contact_details='Contact1', address='Address1', vendor_code='V001')
        Vendor.objects.create(name='Vendor2', contact_details='Contact2', address='Address2', vendor_code='V002')
        
        response = self.client.get(reverse('vendor-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Add more tests for other CRUD operations and edge cases...

class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='Contact Info', address='Vendor Address', vendor_code='V001')
        self.purchase_order_data = {'po_number': 'PO001', 'vendor': self.vendor.id, 'order_date': '2023-01-01T00:00:00Z', 'delivery_date': '2023-01-10T00:00:00Z', 'items': {'item1': 'Description1'}, 'quantity': 10, 'status': 'pending'}

    def test_create_purchase_order(self):
        response = self.client.post(reverse('purchase-order-list-create'), self.purchase_order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 1)

    def test_get_purchase_orders(self):
        PurchaseOrder.objects.create(po_number='PO001', vendor=self.vendor, order_date='2023-01-01T00:00:00Z', delivery_date='2023-01-10T00:00:00Z', items={'item1': 'Description1'}, quantity=10, status='completed')
        PurchaseOrder.objects.create(po_number='PO002', vendor=self.vendor, order_date='2023-01-02T00:00:00Z', delivery_date='2023-01-12T00:00:00Z', items={'item2': 'Description2'}, quantity=20, status='pending')
        
        response = self.client.get(reverse('purchase-order-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Add more tests for other CRUD operations and edge cases...
