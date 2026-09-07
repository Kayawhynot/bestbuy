class Product:
    """Represents a single product available in the store."""

    def __init__(self, name, price, quantity):
        """Create a product. Raises Exception if name is empty
        or price/quantity are negative."""
        if name == "" or price < 0 or quantity < 0:
            raise Exception(
                "Name can't be empty. Price and quantity must be a positive!"
            )
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set a new quantity. Deactivates the product if it reaches 0."""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False

    def is_active(self):
        """Return True if the product is active, otherwise False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print a readable representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """Buy a given quantity of the product and return the total price.
        Raises Exception if quantity is negative or exceeds stock."""
        if quantity <= 0 or quantity > self.quantity:
            raise Exception(
                f"The quantity {quantity} is not available. "
                f"The max. you can order is: {self.quantity}"
            )
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()
