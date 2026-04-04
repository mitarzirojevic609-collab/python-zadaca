#napraviti shopingcart
#add product

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product (self, item):
        self.items.append(item)

    def show_product(self):
        for item in self.items:
            print(item.name)
