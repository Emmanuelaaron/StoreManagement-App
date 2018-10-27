from flask import Flask, jsonify, request
import json
from .models.products import Products
from .models.sales import Sales

products = Products()
sales = Sales()
app = Flask(__name__)

@app.route("/")
def index():
    return "Emma's Storemanagement App"

@app.route("/api/v1/products/", methods=['GET'])
def get_products():
    return jsonify(products.get_products()), 200

@app.route("/api/v1/products/", methods=['POST'])
def add_product():
    return jsonify(products.add_product()), 201
            
@app.route("/api/v1/products/<int:catalog_no>", methods=['GET'])
def get_specific_product(catalog_no):
    return jsonify(products.get_specific_prod(catalog_no)), 200 

@app.route("/api/v1/sales/", methods=['POST'])
def add_sales():
    return jsonify(sales.add_sales()), 201

@app.route("/api/v1/get_sales/", methods=['GET'])
def get_sales():
    return jsonify(sales.get_sales()), 200

@app.route("/api/v1/get_sales/<int:sales_id>", methods=['GET'])
def get_specific_sale(sales_id):
    return jsonify(sales.get_specific_sale(sales_id)), 200
    
if __name__=='__main__':

	app.run(debug=True)

    
