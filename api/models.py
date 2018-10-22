class Products():
    product_list = []

    def get_products(self):
        """Function returns list of products"""
        if len(self.product_list) == 0:
            return "Nothing to get from the store"
        else:
            return self.product_list

