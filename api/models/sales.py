from flask import request
from .products import Products

class Sales():
    sales_records = []
    number_of_sales = 0
    total_price = 0

    def add_sales(self):
        
        sales = {
            "sales_id" : int(request.json["sales_id"]),
            "sold_item" : request.json["sold_item"],
            "price" : request.json["price"]
            
        }

        self.sales_records.append(sales)
        self.number_of_sales =+ len(self.sales_records)
        price = int(sales["price"])
        self.total_price += price
        return self.sales_records

    def get_sales(self):
        if len(self.sales_records) == 0:
            return "No sales yet"
        else:
            return ("No. of sales = "+  str(self.number_of_sales), "and the total price is "+ str(self.total_price))