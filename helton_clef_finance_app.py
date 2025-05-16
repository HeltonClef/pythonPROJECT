
import getpass

# Sample data
users = {
    'clef': 'clef'
}

transactions = []
budget = 0
goal = 0

def login():
    print("==== Welcome to Helton Clef Finance Manager ====")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    if username in users and users[username] == password:
        print("✅ Login successful!\n")
        main_menu()
    else:
        print("❌ Invalid credentials.")
        login()

def add_transaction():
    t_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: $"))
    category = input("Enter category (food, rent, salary, etc.): ").capitalize()
    transactions.append({'type': t_type, 'amount': amount, 'category': category})
    print("✅ Transaction added.\n")

def view_balance():
    income = sum(t['amount'] for t in transactions if t['type'] == 'income')
    expenses = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = income - expenses
    print(f"\n💰 Balance: ${balance:.2f}")
    print(f"📉 Total Expenses: ${expenses:.2f}")
    print(f"📈 Total Income: ${income:.2f}\n")

def view_transactions():
    print("\n📜 Transaction History:")
    for t in transactions:
        color = "\033[92m" if t['type'] == 'income' else "\033[91m"
        print(f"{color}{t['type'].capitalize()}: ${t['amount']:.2f} | {t['category']}\033[0m")
    print("")

def set_budget():
    global budget
    budget = float(input("Enter your monthly budget: $"))
    print("✅ Budget set.\n")

def set_goal():
    global goal
    goal = float(input("Enter your financial goal: $"))
    print("✅ Goal set.\n")

def main_menu():
    while True:
        print("""📌 Main Menu:
1. Add Transaction
2. View Balance
3. View Transaction History
4. Set Monthly Budget
5. Set Financial Goal
6. Exit
""")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_balance()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            set_budget()
        elif choice == '5':
            set_goal()
        elif choice == '6':
            print("👋 Thank you for using Helton Clef Finance Manager.")
            break
        else:
            print("❌ Invalid option. Try again.\n")

# Start app
login()
