from prettytable import PrettyTable

class Admin:
    def __init__(self):
        self.username = 'admin'
        self.password = '1234'
        self.cake_file = "data/cakes.txt"
        self.order_file = "data/orders.txt"

    def login(self):
        user = input("Enter admin username: ")
        pwd = input("Enter password: ")
        if user == self.username and pwd == self.password:
            print("Login successful!")
            self.menu()
        else:
            print("Invalid credentials!")

    def menu(self):
        while True:
            print("\n--- Admin Panel ---")
            print("1. Add Cake")
            print("2. View Cakes")
            print("3. Update Stock")
            print("4. Delete Cake")
            print("5. View Orders")
            print("6. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_cake()
            elif choice == '2':
                self.view_cakes()
            elif choice == '3':
                self.update_stock()
            elif choice == '4':
                self.delete_cake()
            elif choice == '5':
                self.view_orders()
            elif choice == '6':
                break
            else:
                print("Invalid choice!")

    def generate_cake_id(self):
        try:
            with open(self.cake_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                if not lines:
                    return 1
                last_line = lines[-1].strip().split(",")
                return int(last_line[0]) + 1
        except FileNotFoundError:
            return 1

    def add_cake(self):
        cake_id = self.generate_cake_id()
        name = input("Enter cake name: ")
        price = input("Enter cake price: ")
        qty = input("Enter quantity: ")

        with open(self.cake_file, "a", encoding="utf-8") as f:
            f.write(f"{cake_id},{name},{price},{qty}\n")

        print(f"Cake added successfully with ID {cake_id}!")

    def view_cakes(self):
        print("\n--- Available Cakes ---")
        try:
            with open(self.cake_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                print("No cakes available.")
                return

            table = PrettyTable()
            table.field_names = ["Cake ID", "Name", "Price", "Quantity"]

            for line in lines:
                cake_id, name, price, qty = line.strip().split(",")
                table.add_row([cake_id, name, price, qty])

            print(table)

        except FileNotFoundError:
            print("Cake file not found!")

    def update_stock(self):
        cake_id = input("Enter cake ID to update: ")
        new_qty = input("Enter new quantity: ")

        try:
            with open(self.cake_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Cake file not found!")
            return

        new_lines = []
        updated = False

        for line in lines:
            cid, name, price, qty = line.strip().split(",")
            if cid == cake_id:
                new_lines.append(f"{cid},{name},{price},{new_qty}\n")
                updated = True
            else:
                new_lines.append(line)

        with open(self.cake_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        if updated:
            print("Stock updated successfully!")
        else:
                print("Cake ID not found!")

    def delete_cake(self):
        cake_id = input("Enter cake ID to delete: ")

        try:
            with open(self.cake_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print("Cake file not found!")
            return

        new_lines = []
        found = False

        for line in lines:
            cid, name, price, qty = line.strip().split(",")
            if cid != cake_id:
                new_lines.append(line)
            else:
                found = True

        with open(self.cake_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        if found:
            print("Cake deleted successfully!")
        else:
            print("Cake ID not found!")

    def view_orders(self):
        print("\n--- All Orders ---")
        try:
            with open(self.order_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                print("No orders found.")
                return

            table = PrettyTable()
            table.field_names = ["Customer", "Cake", "Qty", "Total"]

            for line in lines:
                user, cake, qty, total = line.strip().split(",")
                table.add_row([user, cake, qty, total])

            print(table)

        except FileNotFoundError:
            print("Orders file not found!")
