from flask import Flask, jsonify, request
import json
from .models import models

from models import models
app = Flask(__name__)

@app.route("/api/v1/products/", methods=['GET'])
def get_products():
    return jsonify(
        models.get_products()
    ), 200
if __name__=='__main__':
	app.run(debug=True)

    
