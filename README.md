# Banking System Console Application

This is a simple console-based banking system developed in Python. The system allows users to create accounts, perform banking transactions (deposit and withdrawal), and manage their finances securely. All account and transaction data are stored using file handling with persistent storage in text files.

## Features

1. **Account Creation:**
   - Allows users to create new accounts by providing their name, initial deposit, and password.
   - Account details (Account Number, Name, Password, Balance) are stored in the `accounts.txt` file.

2. **Secure Login:**
   - Users can log in to their account using the account number and password.
   - Passwords are securely hashed using the SHA-256 algorithm for encryption.

3. **Banking Transactions:**
   - Users can deposit and withdraw money from their account.
   - All transactions are logged in the `transactions.txt` file (Account Number, Transaction Type, Amount, Date).

4. **File Handling:**
   - **Accounts File (`accounts.txt`)**: Stores all user account details.
   - **Transactions File (`transactions.txt`)**: Logs every transaction (Deposit or Withdrawal) made by users.

5. **Error Handling:**
   - Invalid inputs (such as wrong account number, incorrect password, or insufficient balance for withdrawal) are handled gracefully with error messages.

6. **Security:**
   - User passwords are securely stored using SHA-256 hashing, ensuring no plain-text passwords are saved.

## Prerequisites

- Python 3.x

## How to Run

1. **Clone the Repository:**
   - Clone this project to your local machine using:
     ```bash
     git clone https://github.com/your-username/banking-system.git
     ```

2. **Navigate to the Project Directory:**
   - Use `cd` to navigate to the directory where the script is located.

3. **Run the Script:**
   - Execute the Python script in your terminal or command prompt:
     ```bash
     python banking_system.py
     ```

4. **Start Interacting with the System:**
   - The system will display the main menu where you can:
     - Create an account
     - Log in to your account
     - Exit the system

## File Structure
banking-system/ │ ├── banking_system.py # The main Python script 
├── accounts.txt # Stores user account details (Account Number, Name, Password, Balance) 
└── transactions.txt # Logs all user transactions (Account Number, Transaction Type, Amount, Date)

## File Formats

1. **accounts.txt:**
   Each line contains the following format:
   Account Number, Name, Password (hashed), Balance

   Example:123456, John Doe, 5f4dcc3b5aa765d61d8327deb882cf99, 1500

2. **transactions.txt:**
Each line contains the following format:
Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date

Example:
123456, Deposit, 500, 2024-12-23



