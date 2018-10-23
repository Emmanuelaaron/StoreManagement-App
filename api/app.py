from flask import Flask, jsonify, request
import json
from .models import Products

products = Products()
app = Flask(__name__)

@app.route("/api/v1/products/", methods=['GET'])
def get_products():
    return jsonify(products.get_products()), 200

@app.route("/api/v1/products/", methods=['POST'])
def add_product():
    return jsonify(products.add_product()), 200
    

if __name__=='__main__':

	app.run(debug=True)

    
