# Enhanced_BankingApp.py - Creative Multi-Feature Banking System

import os
import json
import datetime
from Model import BankAccount, BankAccountOwner, TransactionType

class EnhancedBankingSystem:
    def __init__(self):
        self.accounts = {}
        self.transaction_history = []
        self.data_file = "banking_data.json"
        self.load_data()
    
    def save_data(self):
        """Save all banking data to JSON file"""
        data = {
            'accounts': {},
            'transaction_history': self.transaction_history
        }
        
        for acc_num, account in self.accounts.items():
            data['accounts'][acc_num] = {
                'account_number': account.account_number,
                'owner_first_name': account.account_owner.first_name,
                'owner_last_name': account.account_owner.last_name,
                'balance': account.account_balance
            }
        
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_data(self):
        """Load banking data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                
                # Restore accounts
                for acc_data in data.get('accounts', {}).values():
                    owner = BankAccountOwner(
                        acc_data['owner_first_name'], 
                        acc_data['owner_last_name']
                    )
                    account = BankAccount(
                        acc_data['account_number'], 
                        owner, 
                        acc_data['balance']
                    )
                    self.accounts[acc_data['account_number']] = account
                
                # Restore transaction history
                self.transaction_history = data.get('transaction_history', [])
                
            except Exception as e:
                print(f"Error loading data: {e}")
                self.create_default_accounts()
        else:
            self.create_default_accounts()
    
    def create_default_accounts(self):
        """Create some default accounts for demo"""
        accounts_data = [
            (123456, "Filan", "Fisteku", 500.0),
            (789012, "John", "Doe", 1000.0),
            (345678, "Jane", "Smith", 750.0),
            (901234, "Alice", "Johnson", 1200.0)
        ]
        
        for acc_num, first, last, balance in accounts_data:
            owner = BankAccountOwner(first, last)
            account = BankAccount(acc_num, owner, balance)
            self.accounts[acc_num] = account
    
    def log_transaction(self, account_number, transaction_type, amount, success=True, error_msg=""):
        """Log transaction for history"""
        transaction = {
            'timestamp': datetime.datetime.now().isoformat(),
            'account_number': account_number,
            'type': transaction_type,
            'amount': amount,
            'success': success,
            'error': error_msg
        }
        self.transaction_history.append(transaction)
    
    def create_account(self):
        """Create a new bank account"""
        print("\n🏦 === CREATE NEW ACCOUNT ===")
        
        # Generate new account number
        account_number = max(self.accounts.keys()) + 1 if self.accounts else 100000
        
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name: ").strip()
        
        try:
            initial_deposit = float(input("Enter initial deposit (minimum $10): $"))
            if initial_deposit < 10:
                print("❌ Minimum initial deposit is $10")
                return
        except ValueError:
            print("❌ Invalid amount")
            return
        
        owner = BankAccountOwner(first_name, last_name)
        account = BankAccount(account_number, owner, initial_deposit)
        self.accounts[account_number] = account
        
        self.log_transaction(account_number, "ACCOUNT_CREATED", initial_deposit)
        self.save_data()
        
        print(f"✅ Account created successfully!")
        print(f"📋 Account Number: {account_number}")
        print(f"👤 Owner: {owner.full_name}")
        print(f"💰 Initial Balance: ${initial_deposit:.2f}")
    
    def transfer_money(self):
        """Transfer money between accounts"""
        print("\n💸 === TRANSFER MONEY ===")
        
        # Initialize variables to avoid unbound errors
        from_acc = None
        amount = None
        
        try:
            from_acc = int(input("From Account Number: "))
            to_acc = int(input("To Account Number: "))
            amount = float(input("Transfer Amount: $"))
            
            if from_acc not in self.accounts:
                print("❌ Source account not found")
                return
            
            if to_acc not in self.accounts:
                print("❌ Destination account not found")
                return
            
            if from_acc == to_acc:
                print("❌ Cannot transfer to the same account")
                return
            
            # Perform transfer
            source_account = self.accounts[from_acc]
            dest_account = self.accounts[to_acc]
            
            source_account.withdraw(amount)
            dest_account.deposit(amount)
            
            self.log_transaction(from_acc, "TRANSFER_OUT", amount)
            self.log_transaction(to_acc, "TRANSFER_IN", amount)
            self.save_data()
            
            print(f"✅ Transfer successful!")
            print(f"💰 ${amount:.2f} transferred from {from_acc} to {to_acc}")
            print(f"📊 Source Balance: ${source_account.account_balance:.2f}")
            print(f"📊 Destination Balance: ${dest_account.account_balance:.2f}")
            
        except ValueError as e:
            if "Insufficient balance" in str(e):
                print("❌ Insufficient balance for transfer")
                if from_acc is not None and amount is not None:
                    self.log_transaction(from_acc, "TRANSFER_FAILED", amount, False, str(e))
            else:
                print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Invalid input: {e}")
    
    def account_summary(self):
        """Show summary of all accounts"""
        print("\n📊 === ACCOUNT SUMMARY ===")
        
        if not self.accounts:
            print("No accounts found.")
            return
        
        total_balance = 0
        print(f"{'Account':<10} {'Owner':<20} {'Balance':<15}")
        print("-" * 50)
        
        for account in self.accounts.values():
            print(f"{account.account_number:<10} {account.account_owner.full_name:<20} ${account.account_balance:<14.2f}")
            total_balance += account.account_balance
        
        print("-" * 50)
        print(f"{'TOTAL':<30} ${total_balance:.2f}")
        print(f"📈 Total Accounts: {len(self.accounts)}")
    
    def transaction_history_report(self):
        """Show transaction history"""
        print("\n📜 === TRANSACTION HISTORY ===")
        
        if not self.transaction_history:
            print("No transactions found.")
            return
        
        # Show last 10 transactions
        recent_transactions = self.transaction_history[-10:]
        
        print(f"{'Time':<20} {'Account':<10} {'Type':<15} {'Amount':<12} {'Status':<10}")
        print("-" * 75)
        
        for trans in recent_transactions:
            timestamp = trans['timestamp'][:19].replace('T', ' ')
            status = "✅ Success" if trans['success'] else "❌ Failed"
            amount_str = f"${trans['amount']:.2f}" if trans['amount'] else "N/A"
            
            print(f"{timestamp:<20} {trans['account_number']:<10} {trans['type']:<15} {amount_str:<12} {status:<10}")
    
    def account_operations(self):
        """Perform operations on a specific account"""
        print("\n🏧 === ACCOUNT OPERATIONS ===")
        
        try:
            acc_num = int(input("Enter Account Number: "))
            
            if acc_num not in self.accounts:
                print("❌ Account not found")
                return
            
            account = self.accounts[acc_num]
            
            while True:
                print(f"\n👤 Account: {acc_num} - {account.account_owner.full_name}")
                print(f"💰 Current Balance: ${account.account_balance:.2f}")
                print("\n1. 💵 Deposit")
                print("2. 💸 Withdraw")
                print("3. 📊 Account Details")
                print("4. 🔙 Back to Main Menu")
                
                choice = input("\nChoose operation (1-4): ").strip()
                
                if choice == '1':
                    amount = None  # Initialize variable
                    try:
                        amount = float(input("Deposit amount: $"))
                        account.deposit(amount)
                        self.log_transaction(acc_num, "DEPOSIT", amount)
                        self.save_data()
                        print(f"✅ Deposited ${amount:.2f}")
                        print(f"💰 New Balance: ${account.account_balance:.2f}")
                    except ValueError as e:
                        print(f"❌ Error: {e}")
                        if amount is not None:
                            self.log_transaction(acc_num, "DEPOSIT_FAILED", amount, False, str(e))
                
                elif choice == '2':
                    amount = None  # Initialize variable
                    try:
                        amount = float(input("Withdrawal amount: $"))
                        account.withdraw(amount)
                        self.log_transaction(acc_num, "WITHDRAW", amount)
                        self.save_data()
                        print(f"✅ Withdrew ${amount:.2f}")
                        print(f"💰 New Balance: ${account.account_balance:.2f}")
                    except ValueError as e:
                        print(f"❌ Error: {e}")
                        if amount is not None:
                            self.log_transaction(acc_num, "WITHDRAW_FAILED", amount, False, str(e))
                
                elif choice == '3':
                    print(f"\n📋 === ACCOUNT DETAILS ===")
                    print(f"Account Number: {account.account_number}")
                    print(f"Owner: {account.account_owner.full_name}")
                    print(f"Balance: ${account.account_balance:.2f}")
                
                elif choice == '4':
                    break
                
                else:
                    print("❌ Invalid choice")
        
        except ValueError:
            print("❌ Invalid account number")
    
    def main_menu(self):
        """Main application menu"""
        while True:
            print("\n" + "="*50)
            print("🏦 ENHANCED BANKING SYSTEM 🏦")
            print("="*50)
            print("1. 🏧 Account Operations")
            print("2. 👥 Create New Account")
            print("3. 💸 Transfer Money")
            print("4. 📊 Account Summary")
            print("5. 📜 Transaction History")
            print("6. 💾 Save & Exit")
            print("="*50)
            
            choice = input("Choose an option (1-6): ").strip()
            
            if choice == '1':
                self.account_operations()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                self.transfer_money()
            elif choice == '4':
                self.account_summary()
            elif choice == '5':
                self.transaction_history_report()
            elif choice == '6':
                self.save_data()
                print("💾 Data saved successfully!")
                print("👋 Thank you for using Enhanced Banking System!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

def main():
    """Main application entry point"""
    print("🎉 Welcome to the Enhanced Banking System!")
    print("Loading your banking data...")
    
    banking_system = EnhancedBankingSystem()
    banking_system.main_menu()

if __name__ == '__main__':
    main()
