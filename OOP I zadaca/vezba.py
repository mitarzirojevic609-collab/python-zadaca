from product import Product
from Shoping_cart import ShoppingCart

iPhone16 = Product("iPhone 16", 1500, 5, "ios")
samsungS23Pro = Product("Samsung S23 Pro", 1200, 200, "android")
samsungA55 = Product("Samsung A55", 500, 5, "android")


phoneCart = ShoppingCart()
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(samsungS23Pro)
phoneCart.add_product(samsungS23Pro)
phoneCart.add_product(samsungS23Pro)

phoneCart.show_product()
print(Product.number_of_types)