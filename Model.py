# Model.py

from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "Deposit"
    WITHDRAW = "Withdraw"

class BankAccountOwner:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name
    
    @property
    def first_name(self):
        return self.__first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"
    
    def __str__(self):
        return self.full_name

class BankAccount:
    def __init__(self, account_number, account_owner, account_balance=0.0):
        self.__account_number = account_number
        self.__account_owner = account_owner
        self.__account_balance = float(account_balance)
    
    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def account_owner(self):
        return self.__account_owner
    
    @property
    def account_balance(self):
        return self.__account_balance
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__account_balance += float(amount)
        return True
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__account_balance:
            raise ValueError("Insufficient balance")
        self.__account_balance -= float(amount)
        return True
    
    def __str__(self):
        return f"Account: {self.__account_number}, Owner: {self.__account_owner}, Balance: ${self.__account_balance:.2f}"
