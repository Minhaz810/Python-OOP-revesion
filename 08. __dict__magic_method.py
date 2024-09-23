class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    def __init__(self,name:str,price:float, quantity:int):
        #run validation
        assert price >= 0 , f"Price {price} is not greater than 0"
        assert quantity >=0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price*self.pay_rate
    
item1 = Item("Phone",200,2)
item2 = Item("Laptop",500,3)

print(Item.__dict__) #prints all attribute for class level
print(item1.__dict__) #prints all attributes for instance level
print(item2.price)


""" If I want to change the pay_rate of one particular instance """

item2.pay_rate = 0.6
item1.apply_discount()
item2.apply_discount()
print(item1.price)
print(item2.price)
