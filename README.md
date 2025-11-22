Student Bank Application 🏦

A generic, command-line interface (CLI) banking application built with Python. This project simulates basic banking operations such as account creation, deposits, withdrawals, and transaction history logging, using a JSON file for data persistence.

📋 Features

User Authentication: Secure Sign-up and Login functionality.

Data Persistence: All user data and logs are saved to accounts_db.json, ensuring data remains available after closing the program.

Account Management:

Deposit: Add funds to your wallet.

Withdraw: Remove funds (with sufficient balance checks).

Check Balance: View current available funds.

Transaction Logs: Detailed "Mini Statement" showing the type of transaction, amount, and timestamp.

Input Validation: Prevents negative numbers and non-numeric inputs.

🛠️ Technologies Used

Language: Python 3.x

Database: JSON (File-based storage)

Libraries: json, os, datetime (Standard Python libraries, no external installs required).

🚀 Getting Started

Prerequisites

Make sure you have Python installed on your system. You can check this by running:

python --version


Installation

Clone this repository:

git clone [https://github.com/yourusername/student-bank-app.git](https://github.com/yourusername/student-bank-app.git)


Navigate to the project directory:

cd student-bank-app


Usage

Run the script using Python:

python bank_app.py


(Note: Replace bank_app.py with the actual name of your python file)

📂 Project Structure

├── bank_app.py         # Main application source code
├── accounts_db.json    # Database file (Auto-generated on first run)
├── README.md           # Project documentation
└── PROJECT_REPORT.md   # Technical report


📸 Screenshots / Usage Example

Main Menu:

1. SIGN UP
2. LOGIN
3. QUIT


User Dashboard:

1. Deposit Cash
2. Withdraw Cash
3. View Balance
4. Mini Statement
5. Logout


🔮 Future Improvements

Implement password hashing (currently stored as plain text) for better security.

Add functionality to transfer money between different users.

Create a GUI using Tkinter or PyQt.

📝 License

This project is open-source and available for educational purposes.