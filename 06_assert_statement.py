"""Lets say we do not want any negative in our Item class"""

class Item:
    def __init__(self,name:str,price:float, quantity:int):
        #run validation
        assert price >= 0 , f"Price {price} is not greater than 0"
        assert quantity >=0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity
    

item1 = Item("Phone",20.20,-1)
print(item1.price)


"""
Note:
1. So far we have learned about instance attribute. Assume we want to create an
   attribute in such a way that all the instances shares the attribute, in that case
   we call them a class attribute

"""
