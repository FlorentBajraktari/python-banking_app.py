# create class Bank
class Bank:
    def __init__(self):
        self.__accounts = {}

    def create_account(self, account_id, holder_name, initial_balance=0):
        if account_id in self.__accounts:
            raise ValueError("Account ID already exists.")
        account = Account(account_id, holder_name, initial_balance)
        self.__accounts[account_id] = account
        return account

    def get_account(self, account_id):
        return self.__accounts.get(account_id, None)

    def perform_transaction(self, account_id, transaction):
        account = self.get_account(account_id)
        if not account:
            raise ValueError("Account not found.")
        if transaction.get_type() == "deposit":
            account.deposit(transaction.get_amount())
        elif transaction.get_type() == "withdrawal":
            account.withdraw(transaction.get_amount())
        else:
            raise ValueError("Invalid transaction type.")
        return account

# create class Account
class Account:
    def __init__(self, account_id, holder_name, balance=0):
        self.__account_id = account_id
        self.__holder_name = holder_name
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_holder_name(self):
        return self.__holder_name

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

# create class Transaction
class Transaction:
    def __init__(self, transaction_type, amount):
        self.__transaction_type = transaction_type
        self.__amount = amount

    def get_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount
