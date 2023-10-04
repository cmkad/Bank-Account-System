from Bank import Bank
from BankAccount import BankAccount

if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. Make Deposit")
        print("3. Make Withdrawal")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_holder = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            account_number = bank.create_account(account_holder, initial_balance)
            print(f"Account created with account number: {account_number}")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            if bank.make_deposit(account_number, amount):
                print("Deposit successful.")
            else:
                print("Invalid account number or amount.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            if bank.make_withdrawal(account_number, amount):
                print("Withdrawal successful.")
            else:
                print("Invalid account number or amount.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            balance = bank.get_account_balance(account_number)
            if balance is not None:
                print(f"Current balance: ${balance:.2f}")
            else:
                print("Invalid account number.")

        elif choice == "5":
            from_account_number = input("Enter your account number: ")
            to_account_number = input("Enter recipient's account number: ")
            amount = float(input("Enter transfer amount: "))
            if bank.transfer(from_account_number, to_account_number, amount):
                print("Transfer successful.")
            else:
                print("Invalid account numbers or insufficient balance.")

        elif choice == "6":
            print("Exiting the bank.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
