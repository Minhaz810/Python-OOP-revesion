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
    
item1 = Item("Phone",200,2)
item2 = Item("Laptop",500,3)
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)