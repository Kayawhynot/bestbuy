class Product:

    def __init__(self, name, price, quantity):
        if name == "" or price < 0 or quantity < 0:
            raise Exception("Name can't be empty. Price and quantity must be a positive!")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity < 0 or quantity > self.quantity:
            raise Exception(f"The quantity {quantity} is not available. The max. you can order is: {self.quantity}")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
