from base_model import Bank, Account, Transaction
from print_utils import print_account_info, print_transaction_info

class BankingApp:
    def __init__(self):
        self.bank = Bank()

    def start(self):
        # Create a new account
        account = self.bank.create_account("12345", "Florent Bajraktari", 1000)
        
        # Perform a deposit
        deposit_transaction = Transaction("deposit", 200)
        self.bank.perform_transaction(account.get_account_id(), deposit_transaction)
        
        # Perform a withdrawal
        withdrawal_transaction = Transaction("withdrawal", 150)
        self.bank.perform_transaction(account.get_account_id(), withdrawal_transaction)
        
        # Print account and transaction information
        print_account_info(account)
        print_transaction_info(deposit_transaction)
        print_transaction_info(withdrawal_transaction)

         # Run the application
if __name__ == "__main__":
    app = BankingApp()
    app.start()
