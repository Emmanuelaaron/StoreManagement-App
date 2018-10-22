from unittest import TestCase
from flask import json
from .views import app
class test_views(TestCase):
    """class that test the code in the views folder"""
    def setUp():
        self.app = app
        self.client = self.app.test_client
    def test_get_product(self):
        products = self.client().get("/api/v1/products/")
        self.assertEqual(products.status_code, 200)



















