class BankAccount:
    def __init__(self, user_id, password, account_number, name, email, phone, account_type, branch, balance=0):
        self.user_id = user_id
        self.password = password
        self.account_number = account_number
        self.name = name
        self.email = email
        self.phone = phone
        self.account_type = account_type
        self.branch = branch
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.name}")
        print(f"Email ID       : {self.email}")
        print(f"Phone Number   : {self.phone}")
        print(f"Account Type   : {self.account_type}")
        print(f"Branch         : {self.branch}")
        print(f"Balance        : ₹{self.balance}")

users = {}

def register():
    print("\n--- Register New Account ---")
    user_id = input("Create a User ID: ")
    if user_id in users:
        print("User ID already exists. Please try a different one.")
        return
    password = input("Create a Password: ")
    account_number = input("Enter Account Number: ")
    name = input("Enter Account Holder Name: ")
    email = input("Enter Email ID: ")
    phone = input("Enter Phone Number: ")
    account_type = input("Enter Account Type (Savings/Current): ")
    branch = input("Enter Branch Name: ")

    account = BankAccount(user_id, password, account_number, name, email, phone, account_type, branch)
    users[user_id] = account
    print("Account registered successfully.")

def login():
    print("\n--- Login ---")
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id in users and users[user_id].password == password:
        print("Login successful.")
        account_menu(users[user_id])
    else:
        print("Invalid credentials. Try again.")

def account_menu(account):
    while True:
        print("\n--- Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account Details")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.display()
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")

# Main Menu
while True:
    print("\n====== Welcome to Python Bank ======")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    main_choice = input("Enter your choice: ")

    if main_choice == '1':
        register()
    elif main_choice == '2':
        login()
    elif main_choice == '3':
        print("Thank you for using Python Bank.")
        break
    else:
        print("Invalid choice. Please try again.")
