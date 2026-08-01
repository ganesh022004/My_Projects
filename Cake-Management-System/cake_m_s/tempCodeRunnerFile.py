from admin import Admin
from customer import Customer

def main():
    while True:
        print("\n--- Welcome to Cake Management System ---")
        print("1. Admin Login")
        print("2. Customer Portal")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            Admin().login()
        elif choice == '2':
            Customer().main_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
