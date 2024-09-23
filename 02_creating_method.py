"""built in method"""

random_string = "abcd"
print(random_string.upper())

"""here .upper() is a method of the builtin string class"""

class Item:

    """
    here self means, when I am calling a method, python passes the object itself to a method as a first argument, we
    can not have the empty parameter in the method
    """
    def calculate_item_price(self):
        pass



item = Item()
item.name = "Laptop"
item.price = 2000
item.quantity = 5
item.calculate_item_price()


"""
Tasks:
1. Try calling the method without self

"""