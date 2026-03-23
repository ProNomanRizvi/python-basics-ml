class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def display(self):
        print(f"\n  Name: {self.name}")
        print(f"  Price: {self.price}")
        print(f"  Quantity: {self.quantity}")
        print(f"  Total Value: {self.total_value()}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Added: {product.name}")

    def most_expensive(self):
        if not self.products:
            return None
        max_product = self.products[0]
        for p in self.products:
            if p.price > max_product.price:
                max_product = p
        return max_product

    def total_inventory_value(self):
        total = 0
        for p in self.products:
            total += p.total_value()
        return total

    def search(self, name):
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def display_all(self):
        if not self.products:
            print("Inventory is empty")
            return
        print("\n=== All Products ===")
        for p in self.products:
            p.display()


def menu():
    print("\n=== Inventory Menu ===")
    print("1. Add Product")
    print("2. Display All")
    print("3. Search Product")
    print("4. Most Expensive")
    print("5. Total Value")
    print("6. Exit")
    return input("Choice: ")


def main():
    inventory = Inventory()

    while True:
        choice = menu()

        if choice == "1":
            name = input("Name: ")
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))
            inventory.add_product(Product(name, price, quantity))

        elif choice == "2":
            inventory.display_all()

        elif choice == "3":
            name = input("Search name: ")
            result = inventory.search(name)
            if result:
                result.display()
            else:
                print("Product not found")

        elif choice == "4":
            result = inventory.most_expensive()
            if result:
                result.display()
            else:
                print("Inventory is empty")

        elif choice == "5":
            print(f"Total Inventory Value: {inventory.total_inventory_value()}")

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()