class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity  = quantity

    def calculate_item_price(self):
        return self.price * self.quantity
    
item1 = Item("Phone",1000,5)

print(item1.calculate_item_price())

"""

Note:
1. We can also assign attribute to an object that is not inside the constructor 

"""

item1.is_large = False
print(item1.is_large)