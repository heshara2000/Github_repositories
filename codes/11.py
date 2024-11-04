# class product:
#     def __init__(self,id,name,price):
#         self.id = id
#         self.name = name
#         self.price = price


# class Cart:
#     def __init__(self):
#         self.items = {}


#     def add_product(self,product,quantity=1):
#         if product.id in self.items:
#             self.items[product.id]["quantity"] +=quantity
#         else:
#             self.items[product.id] = {"product": product}

#     def remove_product(self,product,quantity=1):
#         if product.id in self.items:
#             if self.items[product.id]["quantity"] > quantity:
#                 self.items[product.id]["quantity"] -= quantity
#                 print(f"Removed {quantity} of {product.name} from the cart.")
#             else:
#                 del self.items[product.id]
#                 print(f"Removed all of {product.name} from the cart.")
#         else:
#             print(f"{product.name} is not in the cart.")

#     def cal_total(self):
#         total=0
#         for item in self.items.values():
#             total += item["product"].price * item["quantity"]
#         return total
# if __name__ == "__main__":
#         product1 = product(1,"apple",50)
#         product2 = product(2,"orange",60)
#         product3 = product(3,"banana",70)

#         cart = Cart()

#         cart.add_product(product1,5)
#         cart.add_product(product3,8)

#         cart.remove_product(product1,2)

#         total = cart.cal_total()
#         print(f"total price is {total:.2f}")



    
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.id in self.items:
            self.items[product.id]["quantity"] += quantity
        else:
            self.items[product.id] = {"product": product, "quantity": quantity}

    def remove_product(self, product, quantity=1):
        if product.id in self.items:
            if self.items[product.id]["quantity"] > quantity:
                self.items[product.id]["quantity"] -= quantity
                print(f"Removed {quantity} of {product.name} from the cart.")
            else:
                del self.items[product.id]
                print(f"Removed all of {product.name} from the cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def cal_total(self):
        total = 0
        for item in self.items.values():
            total += item["product"].price * item["quantity"]
        return total


# Correctly placed if __name__ == "__main__":
if __name__ == "__main__":
    product1 = Product(1, "Apple", 50)
    product2 = Product(2, "Orange", 60)
    product3 = Product(3, "Banana", 70)

    cart = Cart()

    cart.add_product(product1, 5)  # Add 5 apples
    cart.add_product(product3, 8)  # Add 8 bananas

    cart.remove_product(product1, 2)  # Remove 2 apples

    total = cart.cal_total()
    print(f"Total price is {total:.2f}")
