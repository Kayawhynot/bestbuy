class Store:
    """Holds a collection of Product objects and manages store-wide
    operations like ordering and inventory totals."""

    def __init__(self, product_list):
        """Create a store with an initial list of products."""
        self.product_list = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove a product from the store."""
        self.product_list.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.product_list:
            total = total + product.get_quantity()
        return total

    def get_all_products(self):
        """Return a list of all active products in the store."""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """Buy multiple products at once. shopping_list is a list of
        (product, quantity) tuples. Returns the total price."""
        total_price = 0
        successful_purchase = []
        for product, amount in shopping_list:
            try:
                total_price += product.buy(amount)
                successful_purchase.append((product, amount))
            except Exception as e:
                print(f"{e}")
        return total_price, successful_purchase
