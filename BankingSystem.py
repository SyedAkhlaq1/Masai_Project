import hashlib
import os
import datetime

# File paths for storing account and transaction data
ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# Function to hash passwords using SHA-256 for security
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to load all accounts from the accounts file
def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r") as file:
            for line in file:
                account_number, name, password, balance = line.strip().split(',')
                accounts[account_number] = {
                    'name': name,
                    'password': password,
                    'balance': float(balance)
                }
    return accounts

# Function to save account details to the accounts file
def save_account(account_number, name, password, balance):
    with open(ACCOUNTS_FILE, "a") as file:
        file.write(f"{account_number},{name},{password},{balance}\n")

# Function to log transactions to the transactions file
def log_transaction(account_number, transaction_type, amount):
    with open(TRANSACTIONS_FILE, "a") as file:
        file.write(f"{account_number},{transaction_type},{amount},{datetime.date.today()}\n")

# Function to create a new account
def create_account(accounts):
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    account_number = str(100000 + len(accounts))  # Simple account number generation
    password = input("Enter a password: ")
    hashed_password = hash_password(password)

    save_account(account_number, name, hashed_password, initial_deposit)
    print(f"Your account number: {account_number}")
    print("Account created successfully!")

    # Add the new account to the in-memory accounts dictionary
    accounts[account_number] = {
        'name': name,
        'password': hashed_password,
        'balance': initial_deposit
    }

# Function to handle user login
def login(accounts):
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    # Check if account exists and password is correct
    if account_number in accounts and accounts[account_number]['password'] == hashed_password:
        print("Login successful!")
        return account_number
    else:
        print("Invalid account number or password.")
        return None

# Function to handle deposit transactions
def deposit(account_number, accounts):
    amount = float(input("Enter amount to deposit: "))
    accounts[account_number]['balance'] += amount
    print(f"Deposit successful! Current balance: {accounts[account_number]['balance']}")
    log_transaction(account_number, "Deposit", amount)

# Function to handle withdrawal transactions
def withdraw(account_number, accounts):
    amount = float(input("Enter amount to withdraw: "))
    if accounts[account_number]['balance'] >= amount:
        accounts[account_number]['balance'] -= amount
        print(f"Withdrawal successful! Current balance: {accounts[account_number]['balance']}")
        log_transaction(account_number, "Withdrawal", amount)
    else:
        print("Insufficient balance.")

# Main function to run the console-based Banking System
def main():
    accounts = load_accounts()

    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)

        elif choice == "2":
            account_number = login(accounts)
            if account_number:
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    transaction_choice = input("Enter your choice: ")

                    if transaction_choice == "1":
                        deposit(account_number, accounts)

                    elif transaction_choice == "2":
                        withdraw(account_number, accounts)

                    elif transaction_choice == "3":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Thank you for using the Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
