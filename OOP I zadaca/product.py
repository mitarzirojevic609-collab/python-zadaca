


class Product:
    number_of_product = 0
    allowed_types = ["android", "ios"]
    number_of_types = {
        'android' : 0,
        'ios' : 0,
    }

    def __init__(self, name, price, amount, type):

        if amount < 1:
            raise ValueError("Amount mus be more than 0")

        if type not in Product.allowed_types:
            raise ValueError("you didnt pass the correct type")


        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_product += 1

        Product.number_of_types[type] += amount

