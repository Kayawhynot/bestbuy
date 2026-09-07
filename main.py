from store import Store
from products import Product


def start(store):
    """Show the store menu and handle user input until Quit is chosen."""
    while True:
        print("1. List all products in store ")
        print("2. Show total amount in store ")
        print("3. Make an order ")
        print("4. Quit")
        choice = input("Please enter a menu number: ")

        if choice == "1":
            print("Here are all products in our store: ")
            for product in store.get_all_products():
                product.show()

        elif choice == "2":
            print(f" The total quantity in store is: {store.get_total_quantity()}")

        # TODO (für Best Buy 2.0): Bei zu großer Bestellmenge dem Nutzer
        # die verfügbare Restmenge als Alternative anbieten statt nur abzulehnen.
        # Ablauf: Nutzer will z.B. 6x kaufen, aber nur 5 verfügbar ->
        #   "Nur noch 5 verfügbar. Stattdessen 5 kaufen? (y/n)"
        #   bei "y": amount auf product.get_quantity() reduzieren, dann kaufen
        #   bei "n": Position überspringen (aktuelles Verhalten)
        # Prüfung müsste VOR dem Anhängen an shopping_list passieren, nicht erst
        # in Product.buy() -- sonst zu spät für eine Rückfrage an den Nutzer.
        elif choice == "3":
            shopping_list = []
            for product in store.get_all_products():
                product.show()

            while True:
                chosen_product = input("Please type in your product: ")
                product_amount = int(input("Please type in your desired amount: "))
                exit_process = input("To finish your buying process type 'y' or enter to continue: ")

                for product in store.get_all_products():
                    if product.name.lower() == chosen_product.lower():
                        shopping_list.append((product, product_amount))

                if exit_process == "y":
                    break

            total_price, successful_purchase = store.order(shopping_list)

            summary = {}
            for product, amount in successful_purchase:
                summary[product.name] = summary.get(product.name, 0) + amount

            summary_text = ", ".join(
                f"{amount}x {name}" for name, amount in summary.items()
            )

            if not successful_purchase:
                print("Your order couldn't be placed. Please try a different product or amount.")
            else:
                print(
                    f"Thanks for your order! You have ordered {summary_text} "
                    f"with a total amount of {total_price}."
                )

        elif choice == "4":
            print("Thanks for visiting Best Buy!")
            break


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        Product("t", price=1, quantity=5)
    ]
    best_buy = Store(product_list)
    start(best_buy)