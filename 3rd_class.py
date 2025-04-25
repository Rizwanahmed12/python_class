import json
import os 

CONTACT_FILE = "contact.json"

def load_contact():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return {}

def save_contact(contact):
    with open(CONTACT_FILE, "w") as file:  # Corrected here
        json.dump(contact, file, indent=4)

def add_contact(name, email, phone):
    contact = load_contact()
    contact[name] = {"Phone": phone, "Email": email}
    save_contact(contact)
    print("Phone number has been saved")

def search_contact(name):
    contact = load_contact()
    if name in contact:
        return contact[name]
    else:
        return "Contact Not Found"

def update_contact(name, phone=None, email=None):
    contact = load_contact()
    if name in contact:
        if phone:
            contact[name]["Phone"] = phone
        if email:
            contact[name]["Email"] = email
        save_contact(contact)
        print("Contact has been updated!")
    else:
        print("Contact Not Found")

def del_contact(name):
    contact = load_contact()
    if name in contact:
        del contact[name]
        save_contact(contact)
        print("Contact has been deleted!")
    else:
        print("Contact Not Found")

if __name__ == "__main__":
    while True:
        print("\n  Contact Book! ")
        print("1. Add Contact.")
        print("2. Search Contact.")
        print("3. Update Contact.")
        print("4. Delete Contact.")
        print("5. Show all Contacts.")
        print("6. Exit.")
        
        choice = int(input("Enter your desired option! "))
        
        if choice == 1:
            name = input("Enter your Name: ")
            phone = input("Enter your Phone Number: ") 
            email = input("Enter your Email address: ")
            add_contact(name, phone, email)
        
        elif choice == 2:
            name = input("Search your Contact by name: ")
            print(search_contact(name))
        
        elif choice == 3:
            name = input("Name to Update: ")
            phone = input("New Phone (press enter to skip): ")
            email = input("New Email (press enter to skip): ")   
            update_contact(name, phone if phone else None, email if email else None)
        
        elif choice == 4:
            name = input("Enter your name: ")
            del_contact(name)
        
        elif choice == 5:
            contact = load_contact()
            for name, details in contact.items():  # Fixed here
                print(f"{name} - {details}")
        
        elif choice == 6:
            print("Exit from Contact Book!")
            break
        
        else:
            print("You have entered an invalid choice! Try again.")
            
            
        
# Sir Code

# A dictionary to store account information (account holder name and balance)
accounts = {}

def show_menu():
    print("\n----Menu----")
    print("1. Balance Show")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def add_account():
    name = input("Enter the account holder's name: ")
    if name in accounts:
        print("Account already exists!")
    else:
        accounts[name] = 100  # Initial balance is set to 100
        print(f"Account for {name} has been created with an initial balance of 100.")

def select_account():
    print("\n----Existing Accounts----")
    for account in accounts:
        print(account)
    name = input("Enter the name of the account holder you want to access: ")
    return name

def account_operations(account_name):
    balance = accounts[account_name]
    
    while True:
        show_menu()
        select = int(input("Enter your Option '1-4': "))

        if select == 1:
            print(f"Your balance is: {balance}")
        elif select == 2:
            amount = int(input("Enter your Amount to deposit: "))
            if amount < 0:
                print("Amount cannot be negative. Please try again.")
            else:
                balance += amount
                accounts[account_name] = balance  # Update the account balance
                print(f"Amount has been added. New balance: {balance}")
        elif select == 3:
            amount = int(input("Enter Your Amount to withdraw: "))
            if amount < 0:
                print("Withdrawal amount cannot be negative. Please try again.")
            elif amount > balance:
                print("Insufficient balance! You cannot withdraw more than your balance.")
            else:
                balance -= amount
                accounts[account_name] = balance  # Update the account balance
                print(f"Amount has been withdrawn. Your new balance is: {balance}")
        elif select == 4:
            print("Thank you for using this machine!")
            break
        else:
            print("Invalid input! Please enter a number between 1 and 4.")

while True:
    print("\n----Welcome to the Bank----")
    print("1. Add new account")
    print("2. Select existing account")
    print("3. Exit")

    option = int(input("Enter your option '1-3': "))
    
    if option == 1:
        add_account()
    elif option == 2:
        if len(accounts) == 0:
            print("No accounts found. Please create an account first.")
        else:
            account_name = select_account()
            if account_name in accounts:
                account_operations(account_name)  # Perform operations for the selected account
            else:
                print("Account not found!")
    elif option == 3:
        print("Thank you for using the system!")
        break
    else:
        print("Invalid input! Please enter a number between 1 and 3.")