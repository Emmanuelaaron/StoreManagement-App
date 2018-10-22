from unittest import TestCase
from flask import json
from .app import app
class test_run(TestCase):
    """class that test the code in the views folder"""
    def setUp(self):
        self.app = app
        self.client = app.test_client(self)
        product = {
            "product_name": "sodium", 
            "catalog_no": 6756,
            "price": 898,
            "Pack_size": "2kg/pk"
        }
    def test_get_product(self):
        rp = self.client.get("/api/v1/products/")
        self.assertEqual(rp.status_code, 200)



















