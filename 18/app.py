"""
Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.
"""





class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Price is being deleted")
        del self._price

product = Product("Laptop", 1000)

print(product.price)

product.price = 1200
print(product.price)

product.price = -500

del product.price
