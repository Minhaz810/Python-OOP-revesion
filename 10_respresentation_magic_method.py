class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self,name:str,price:float, quantity:int):
        #run validation
        assert price >= 0 , f"Price {price} is not greater than 0"
        assert quantity >=0, f"Quantity {quantity} is not greater than 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions while initializing
        Item.all.append(self) #will pass every instance

    def calculate_item_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price*self.pay_rate
    def __repr__(self):
        return f"Item('{self.name}','{self.price}','{self.quantity}')"  #best practice


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)