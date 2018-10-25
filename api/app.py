from flask import Flask, jsonify, request
import json
from .models.products import Products
from .models.sales import Sales

products = Products()
sales = Sales()
app = Flask(__name__)

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
    return jsonify(sales.add_sales()), 200
    
if __name__=='__main__':

	app.run(debug=True)

    
