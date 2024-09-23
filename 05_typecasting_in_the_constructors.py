class Item:
    def __init__(self,name:str,price:float, quantity:int):
        if not isinstance(name,str):
            raise "must be an string value"
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_item_price(self):
        return self.price * self.quantity
    

item1 = Item("Phone",20.20,20)
print(item1.price)
