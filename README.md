Student Bank Application 🏦

A CLI (Command Line Interface) based banking system built with Python. This application allows users to create accounts, manage their wallet balance, and track transaction history using a local JSON database for persistence.

📋 Features

User Authentication:

- Secure Sign-up (username uniqueness check).

- Login system with password validation.

Wallet Management:

- Deposit: Add funds to the account.

- Withdraw: Remove funds with overdraft protection (checks for sufficient balance).

- Check Balance: View current available funds.

Transaction History:

1. Maintains a log of all credits and debits with timestamps.

2. "Mini Statement" feature to print logs to the console.

Data Persistence:

1. All user data and logs are saved automatically to accounts_db.json.

2. Data remains available even after closing and restarting the program.

🛠️ Technology Stack

- Language: Python 3.x

- Storage: JSON (File Handling)

- Modules: os, json, datetime

🚀 Getting Started

- Prerequisites

- Ensure you have Python installed on your machine. You can check this by running:

  python --version


Installation

Clone this repository:

git clone https://github.com/subhammohanty-sys/Bank-Managment-System


Navigate to the project directory:

  cd student-bank-app


Usage

Run the application:

  python bank_app.py



Follow the on-screen prompts to Register (1) or Login (2).

📂 Project Structure

├── bank_app.py         # Main application logic
├── accounts_db.json    # Database file (Auto-generated on first run)
├── PROBLEM_STATEMENT.md # Project requirements
└── README.md           # Documentation


🔮 Future Improvements

1. Implement password hashing (currently stored as plain text for simplicity).

2. Add an Admin mode to view all users.

3. Implement fund transfers between different users.

🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.
