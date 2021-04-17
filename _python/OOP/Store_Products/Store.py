class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    
    def sell_product(self, id):
        for i in range(len(self.products)):
            if(self.products[i].id == id):
                print(id, " " , self.products[i].id)
                self.products.pop(i)
                print("The following Product has been sold:\n")
                self.products[i].print_info()
                break
        return self
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self
    
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self
    
    def print_products(self):
        for product in self.products:
            product.print_info()
        return self

