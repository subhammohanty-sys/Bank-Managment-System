import json
import os
from datetime import datetime

DATA_FILE = "accounts_db.json"

def get_records():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                return json.load(file)
        except:
            return {}
    return {}

def update_records(database):
    with open(DATA_FILE, 'w') as file:
        json.dump(database, file, indent=4)

class BankingSystem:
    def __init__(self, username):
        self.user = username
        self.db = get_records()
        self.account = self.db.get(username)

    def refresh_db(self):
        self.db = get_records()
        self.account = self.db[self.user]

    def check_funds(self):
        self.refresh_db()
        return self.account['wallet']

    def add_money(self, val):
        self.refresh_db()
        self.account['wallet'] += val
        
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"Credited: {val} | Time: {ts}"
        self.account['logs'].append(entry)
        
        self.db[self.user] = self.account
        update_records(self.db)
        print(f"Deposited successfully. Current Balance: {self.account['wallet']}")

    def remove_money(self, val):
        self.refresh_db()
        if self.account['wallet'] >= val:
            self.account['wallet'] -= val
            
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            entry = f"Debited: {val} | Time: {ts}"
            self.account['logs'].append(entry)
            
            self.db[self.user] = self.account
            update_records(self.db)
            print(f"Withdrawal complete. Remaining Balance: {self.account['wallet']}")
        else:
            print("Transaction failed: Insufficient funds.")

    def print_statement(self):
        self.refresh_db()
        print("\n--- Transaction Logs ---")
        if not self.account['logs']:
            print("No records found.")
        else:
            for log in self.account['logs']:
                print(log)

print("=== STUDENT BANK APPLICATION ===")

active_session = None

while True:
    if active_session is None:
        print("\n1. SIGN UP")
        print("2. LOGIN")
        print("3. QUIT")
        
        opt = input("Select option: ")

        if opt == '1':
            uid = input("Create Username: ")
            records = get_records()
            
            if uid in records:
                print("Username taken.")
            elif not uid:
                print("Invalid username.")
            else:
                pwd = input("Create Password: ")
                records[uid] = {
                    "pass_key": pwd,
                    "wallet": 0.0,
                    "logs": []
                }
                update_records(records)
                print("Registration complete.")

        elif opt == '2':
            uid = input("Username: ")
            records = get_records()
            
            if uid in records:
                pwd = input("Password: ")
                if records[uid]['pass_key'] == pwd:
                    print("Login Successful.")
                    active_session = uid
                else:
                    print("Incorrect password.")
            else:
                print("User does not exist.")
        
        elif opt == '3':
            print("System shutting down.")
            break
        else:
            print("Invalid selection.")

    else:
        print(f"\nUser: {active_session}")
        print("1. Deposit Cash")
        print("2. Withdraw Cash")
        print("3. View Balance")
        print("4. Mini Statement")
        print("5. Logout")
        
        choice = input("Enter code: ")
        user_obj = BankingSystem(active_session)

        if choice == '1':
            try:
                amount = float(input("Amount to add: "))
                if amount > 0:
                    user_obj.add_money(amount)
                else:
                    print("Enter positive value only.")
            except ValueError:
                print("Please enter numbers only.")

        elif choice == '2':
            try:
                amount = float(input("Amount to withdraw: "))
                if amount > 0:
                    user_obj.remove_money(amount)
                else:
                    print("Enter positive value only.")
            except ValueError:
                print("Please enter numbers only.")

        elif choice == '3':
            bal = user_obj.check_funds()
            print(f"Available Balance: {bal}")

        elif choice == '4':
            user_obj.print_statement()

        elif choice == '5':
            active_session = None
            print("Logged out successfully.")
        
        else:
            print("Unknown command.")