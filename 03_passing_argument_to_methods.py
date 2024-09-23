class Item:
    def calculate_item_price(self,x,y):
        return x*y



item = Item()
item.name = "Laptop"
item.price = 2000
item.quantity = 3
print(item.calculate_item_price(item.price,item.quantity))

"""Here it is taking item.price as x and item.quantity as y"""

item2 = Item()
item2.name = "Phone"
item2.price = 500
item2.quantity = 5

print(item2.calculate_item_price(item2.price,item2.quantity))