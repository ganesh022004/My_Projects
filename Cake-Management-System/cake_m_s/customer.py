from prettytable import PrettyTable
from datetime import datetime

class Customer:
    def __init__(self):
        self.cake_file = "data/cakes.txt"
        self.order_file = "data/orders.txt"
        self.bill_file = "data/bill.txt"
        self.user_file = "data/customers.txt"
        self.current_user = None

    def main_menu(self):
        while True:
            print("\n--- Customer System ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.register_customer()
            elif choice == '2':
                self.login_customer()
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")

    def register_customer(self):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        with open(self.user_file, "a", encoding="utf-8") as f:
            f.write(f"{name},{email},{password}\n")

        print("Registration successful!")

    def login_customer(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        try:
            with open(self.user_file, "r", encoding="utf-8") as f:
                for line in f:
                    name, mail, pwd = line.strip().split(",")
                    if mail == email and pwd == password:
                        self.current_user = name
                        print(f"Welcome, {self.current_user}!")
                        self.menu()
                        return

            print("Invalid email or password!")

        except FileNotFoundError:
            print("Customer file not found!")

    def menu(self):
        while True:
            print(f"\n--- Welcome {self.current_user} ---")
            print("1. View Cakes")
            print("2. Order Cake")
            print("3. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_cakes()
            elif choice == '2':
                self.order_cake()
            elif choice == '3':
                print("Logged out successfully!")
                self.current_user = None
                break
            else:
                print("Invalid choice!")

    def view_cakes(self):
        print("\n--- Cake Menu ---")

        try:
            with open(self.cake_file, "r", encoding="utf-8") as f:
                lines = f.readlines()

            if not lines:
                print("No cakes available.")
                return

            table = PrettyTable()
            table.field_names = ["Cake ID", "Name", "Price", "Available"]

            for line in lines:
                cid, name, price, qty = line.strip().split(",")
                table.add_row([cid, name, price, qty])

            print(table)

        except FileNotFoundError:
            print("Cake file not found!")

    def order_cake(self):
        cake_id = input("Enter cake ID: ")
        try:
            order_qty = int(input("Enter quantity: "))
        except ValueError:
            print("Quantity must be a number!")
            return
            
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
            if cid == cake_id:
                found = True
                if int(qty) >= order_qty:
                    total = int(price) * order_qty
                    new_qty = int(qty) - order_qty
                    new_lines.append(f"{cid},{name},{price},{new_qty}\n")

                    with open(self.order_file, "a", encoding="utf-8") as o:
                        o.write(f"{self.current_user},{name},{order_qty},{total}\n")

                    self.generate_bill(cid, name, order_qty, price, total)
                    print(f"Order placed! Total = Rs{total}")

                else:
                    print("Not enough stock!")
                    new_lines.append(line)
            else:
                new_lines.append(line)

        if not found:
            print("Cake ID not found!")

        with open(self.cake_file, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

    def generate_bill(self, cid, name, qty, price, total):
        now = datetime.now().strftime("%d-%m-%Y %H:%M")
        with open(self.bill_file, "w", encoding="utf-8") as b:
            b.write("------ Cake Bill ------\n")
            b.write(f"Date: {now}\n")
            b.write(f"Cake ID: {cid}\n")
            b.write(f"Cake Name: {name}\n")
            b.write(f"Quantity: {qty}\n")
            b.write(f"Price (each): Rs{price}\n")
            b.write(f"Total: Rs{total}\n")
            b.write("------------------------\n")
            b.write("Thank you! Visit Again!\n")
