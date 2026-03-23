class Product:
    def __init__(self, name, price=0, quantity=0):
        self.name = name
        self._price = price
        self._quantity = quantity

    def get_price(self):
        return self._price

    def get_quantity(self):
        return self._quantity

    def set_price(self, price):
        if price <= 0:
            print("Invalid price. Must be greater than 0.")
            return
        self._price = price
        print(f"Price updated to {self._price}")

    def set_quantity(self, qty):
        if qty < 0:
            print("Invalid quantity. Cannot be negative.")
            return
        self._quantity = qty
        print(f"Quantity updated to {self._quantity}")

    def display(self):
        print(f"Name: {self.name} | Price: {self._price} | Qty: {self._quantity}")

    def __str__(self):
        return f"Product: {self.name} | Price: {self._price} | Qty: {self._quantity}"

    def __repr__(self):
        return f"Product(name='{self.name}', price={self._price}, quantity={self._quantity})"


def main():
    product = Product("Default")

    while True:
        print("\n1. Create Product\n2. Update Price\n3. Update Quantity\n4. View Product\n5. Exit")
        choice = int(input("Choice: "))

        if choice == 1:
            name = input("Product Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))
            product = Product(name, price, qty)
            print(product)

        elif choice == 2:
            price = float(input("New Price: "))
            product.set_price(price)

        elif choice == 3:
            qty = int(input("New Quantity: "))
            product.set_quantity(qty)

        elif choice == 4:
            product.display()
            print(repr(product))

        elif choice == 5:
            print("Exiting.")
            break

        else:
            print("Invalid input")


if __name__ == "__main__":
    main()