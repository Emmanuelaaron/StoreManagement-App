from unittest import TestCase
from flask import json
import json
from .app import app
class test_run(TestCase):
    """class that test the code in the views folder"""
    def setUp(self):
        self.app = app
        self.client = app.test_client()

        self.product = {
            "product_name": "sodium", 
            "catalog_no": 6756,
            "price": 898,
            "Pack_size": "2kg/pk"
        }

        self.sales = {
            "sales_id": 89,
            "sold_item": "chromium",
            "price": 989
        }

    def test_get_product(self):
        rp = self.client.get("/api/v1/products/")
        self.assertEqual(rp.status_code, 200)

    def test_add_product(self):
        rp = self.client.post("/api/v1/products/",
        data=json.dumps(self.product),
        content_type='application/json')
        self.assertTrue(rp.data)

    def test_get_specific_prod(self):
        rp = self.client.get("/api/v1/products/6756")
        # data = json.loads(rp.data)
        self.assertEqual(rp.status_code, 200)
        # self.assertIn("sodium", str(data["product_name"]))

    def test_add_sales(self):
        rp = self.client.post("/api/v1/sales/",
        data=json.dumps(self.sales),
        content_type='application/json')
        self.assertTrue(rp.data)

    def test_get_sales(self):
        rp = self.client.get("/api/v1/get_sales/")
        self.assertEqual(rp.status_code, 200)

    def test_get_specific_sale(self):
        rp = self.client.get("/api/v1/get_sales/89")
        self.assertEqual(rp.status_code, 200)


    



















