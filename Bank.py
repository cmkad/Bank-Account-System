from BankAccount import BankAccount
#Create a Bank class that can manage mulitple bank accounts
class Bank:
    def __init__(self):
        self.accounts = {}  # A dictionary to store accounts, where the account number is the key.

    def create_account(self, account_holder, initial_balance=0.0):
        # Generate a unique account number (you can implement your own logic here)
        account_number = str(len(self.accounts) + 1)
        
        # Create a new BankAccount object and store it in the dictionary
        account = BankAccount(account_number, account_holder, initial_balance)
        self.accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        # Retrieve the BankAccount object using the account number as the key
        return self.accounts.get(account_number)

    def make_deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.deposit(amount)
        return False

    def make_withdrawal(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def get_account_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.get_balance()
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                return True
        return False
