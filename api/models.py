from flask import request


class Products():
    product_list = []

    def get_products(self):
        """Function returns list of products"""
        if len(self.product_list) == 0:
            return "Nothing to get from the store"
        else:
            return self.product_list
    
    def add_product(self):
        """This function adds a specified product to the store"""
        product = {
            "product_name": request.json["product_name"],
            "catalog_no": int(request.json["catalog_no"]),
            "price": request.json["price"],
            "pack_size": request.json["pack_size"]
        }
        self.product_list.append(product)
        return product

