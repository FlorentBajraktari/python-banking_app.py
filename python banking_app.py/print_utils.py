def print_account_info(account):
    print(f"Account ID: {account.get_account_id()}")
    print(f"Holder Name: {account.get_holder_name()}")
    print(f"Balance: {account.get_balance()}")

def print_transaction_info(transaction):
    print(f"Transaction Type: {transaction.get_type()}")
    print(f"Amount: {transaction.get_amount()}")
