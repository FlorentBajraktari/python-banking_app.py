# Professional_Banking_GUI.py - Modern CRUD Banking Interface (Fixed)

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import datetime
from Model import BankAccount, BankAccountOwner, TransactionType

class ProfessionalBankingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 Professional Banking System - CRUD Interface")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')
        
        # Data storage
        self.data_file = "banking_data.json"
        self.accounts = {}
        self.transaction_history = []
        
        # Load existing data
        self.load_data()
        
        # Configure styles
        self.setup_styles()
        
        # Create main interface
        self.create_interface()
        
        # Load initial data
        self.refresh_account_list()
        
    def setup_styles(self):
        """Setup custom styles for professional look"""
        style = ttk.Style()
        
        # Configure button styles
        style.configure('Primary.TButton', 
                       font=('Arial', 10, 'bold'),
                       foreground='white')
        
        style.configure('Success.TButton',
                       font=('Arial', 9),
                       foreground='green')
        
        style.configure('Danger.TButton',
                       font=('Arial', 9),
                       foreground='red')
        
        # Configure frame styles
        style.configure('Card.TFrame',
                       relief='raised',
                       borderwidth=2)
        
        # Configure label styles
        style.configure('Title.TLabel',
                       font=('Arial', 16, 'bold'),
                       foreground='#2c3e50')
        
        style.configure('Subtitle.TLabel',
                       font=('Arial', 12, 'bold'),
                       foreground='#34495e')
    
    def create_interface(self):
        """Create the main GUI interface"""
        # Main container
        main_container = ttk.Frame(self.root, padding="10")
        main_container.grid(row=0, column=0, sticky="nsew")
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_container.columnconfigure(1, weight=1)
        main_container.rowconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_container, 
                               text="🏦 Professional Banking System", 
                               style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Left panel - Account Management
        self.create_account_management_panel(main_container)
        
        # Center panel - Account Details
        self.create_account_details_panel(main_container)
        
        # Right panel - Transactions
        self.create_transaction_panel(main_container)
        
        # Bottom panel - Statistics
        self.create_statistics_panel(main_container)
    
    def create_account_management_panel(self, parent):
        """Create account management panel (CRUD operations)"""
        # Account Management Frame
        account_frame = ttk.LabelFrame(parent, text="📋 Account Management", 
                                     style='Card.TFrame', padding="10")
        account_frame.grid(row=1, column=0, sticky="nsew", 
                          padx=(0, 10))
        
        # Create Account Section
        create_label = ttk.Label(account_frame, text="Create New Account", 
                               style='Subtitle.TLabel')
        create_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # First Name
        ttk.Label(account_frame, text="First Name:").grid(row=1, column=0, sticky=tk.W)
        self.first_name_var = tk.StringVar()
        first_name_entry = ttk.Entry(account_frame, textvariable=self.first_name_var, width=20)
        first_name_entry.grid(row=1, column=1, pady=2)
        
        # Last Name
        ttk.Label(account_frame, text="Last Name:").grid(row=2, column=0, sticky=tk.W)
        self.last_name_var = tk.StringVar()
        last_name_entry = ttk.Entry(account_frame, textvariable=self.last_name_var, width=20)
        last_name_entry.grid(row=2, column=1, pady=2)
        
        # Initial Balance
        ttk.Label(account_frame, text="Initial Balance:").grid(row=3, column=0, sticky=tk.W)
        self.balance_var = tk.StringVar(value="0.00")
        balance_entry = ttk.Entry(account_frame, textvariable=self.balance_var, width=20)
        balance_entry.grid(row=3, column=1, pady=2)
        
        # Create Button
        create_btn = ttk.Button(account_frame, text="✅ Create Account", 
                              command=self.create_account, style='Primary.TButton')
        create_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Separator
        ttk.Separator(account_frame, orient='horizontal').grid(row=5, column=0, 
                                                              columnspan=2, sticky="we", pady=10)
        
        # Account List
        list_label = ttk.Label(account_frame, text="Existing Accounts", 
                             style='Subtitle.TLabel')
        list_label.grid(row=6, column=0, columnspan=2, pady=(0, 10))
        
        # Account Listbox with Scrollbar
        list_frame = ttk.Frame(account_frame)
        list_frame.grid(row=7, column=0, columnspan=2, sticky="nsew")
        
        self.account_listbox = tk.Listbox(list_frame, height=8, width=35)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.account_listbox.yview)
        self.account_listbox.configure(yscrollcommand=scrollbar.set)
        
        self.account_listbox.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Bind selection event
        self.account_listbox.bind('<<ListboxSelect>>', self.on_account_select)
        
        # CRUD Buttons
        button_frame = ttk.Frame(account_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="📝 Update", 
                  command=self.update_account, style='Success.TButton').grid(row=0, column=0, padx=2)
        ttk.Button(button_frame, text="🗑️ Delete", 
                  command=self.delete_account, style='Danger.TButton').grid(row=0, column=1, padx=2)
        ttk.Button(button_frame, text="🔄 Refresh", 
                  command=self.refresh_account_list).grid(row=0, column=2, padx=2)
    
    def create_account_details_panel(self, parent):
        """Create account details panel"""
        details_frame = ttk.LabelFrame(parent, text="📊 Account Details", 
                                     style='Card.TFrame', padding="10")
        details_frame.grid(row=1, column=1, sticky="nsew", 
                          padx=10)
        details_frame.columnconfigure(0, weight=1)
        
        # Account Info Display
        self.account_info_text = tk.Text(details_frame, height=12, width=50, 
                                       wrap=tk.WORD, state=tk.DISABLED,
                                       font=('Courier', 10))
        info_scrollbar = ttk.Scrollbar(details_frame, orient="vertical", 
                                     command=self.account_info_text.yview)
        self.account_info_text.configure(yscrollcommand=info_scrollbar.set)
        
        self.account_info_text.grid(row=0, column=0, sticky="nsew")
        info_scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Account Operations
        ops_frame = ttk.LabelFrame(details_frame, text="💰 Quick Operations", padding="10")
        ops_frame.grid(row=1, column=0, columnspan=2, sticky="we", pady=10)
        
        # Amount Entry
        ttk.Label(ops_frame, text="Amount:").grid(row=0, column=0, sticky=tk.W)
        self.operation_amount_var = tk.StringVar()
        amount_entry = ttk.Entry(ops_frame, textvariable=self.operation_amount_var, width=15)
        amount_entry.grid(row=0, column=1, padx=5)
        
        # Operation Buttons
        btn_frame = ttk.Frame(ops_frame)
        btn_frame.grid(row=0, column=2, columnspan=2, padx=10)
        
        ttk.Button(btn_frame, text="💵 Deposit", 
                  command=self.quick_deposit, style='Success.TButton').grid(row=0, column=0, padx=2)
        ttk.Button(btn_frame, text="💸 Withdraw", 
                  command=self.quick_withdraw, style='Danger.TButton').grid(row=0, column=1, padx=2)
    
    def create_transaction_panel(self, parent):
        """Create transaction panel"""
        trans_frame = ttk.LabelFrame(parent, text="🔄 Transactions", 
                                   style='Card.TFrame', padding="10")
        trans_frame.grid(row=1, column=2, sticky="nsew", 
                        padx=(10, 0))
        
        # Transfer Section
        transfer_frame = ttk.LabelFrame(trans_frame, text="💸 Transfer Money", padding="10")
        transfer_frame.grid(row=0, column=0, sticky="we", pady=(0, 10))
        
        # From Account
        ttk.Label(transfer_frame, text="From Account:").grid(row=0, column=0, sticky=tk.W)
        self.from_account_var = tk.StringVar()
        from_combo = ttk.Combobox(transfer_frame, textvariable=self.from_account_var, 
                                 width=15, state="readonly")
        from_combo.grid(row=0, column=1, pady=2)
        self.from_account_combo = from_combo
        
        # To Account
        ttk.Label(transfer_frame, text="To Account:").grid(row=1, column=0, sticky=tk.W)
        self.to_account_var = tk.StringVar()
        to_combo = ttk.Combobox(transfer_frame, textvariable=self.to_account_var, 
                               width=15, state="readonly")
        to_combo.grid(row=1, column=1, pady=2)
        self.to_account_combo = to_combo
        
        # Transfer Amount
        ttk.Label(transfer_frame, text="Amount:").grid(row=2, column=0, sticky=tk.W)
        self.transfer_amount_var = tk.StringVar()
        ttk.Entry(transfer_frame, textvariable=self.transfer_amount_var, 
                 width=18).grid(row=2, column=1, pady=2)
        
        # Transfer Button
        ttk.Button(transfer_frame, text="🔄 Transfer", 
                  command=self.transfer_money, style='Primary.TButton').grid(row=3, column=0, 
                                                                           columnspan=2, pady=10)
        
        # Transaction History
        history_frame = ttk.LabelFrame(trans_frame, text="📜 Recent Transactions", padding="10")
        history_frame.grid(row=1, column=0, sticky="nsew")
        
        # Transaction Treeview
        columns = ("Time", "Account", "Type", "Amount", "Status")
        self.transaction_tree = ttk.Treeview(history_frame, columns=columns, 
                                           show="headings", height=8)
        
        # Configure columns
        for col in columns:
            self.transaction_tree.heading(col, text=col)
            self.transaction_tree.column(col, width=80)
        
        # Scrollbar for treeview
        tree_scroll = ttk.Scrollbar(history_frame, orient="vertical", 
                                  command=self.transaction_tree.yview)
        self.transaction_tree.configure(yscrollcommand=tree_scroll.set)
        
        self.transaction_tree.grid(row=0, column=0, sticky="nsew")
        tree_scroll.grid(row=0, column=1, sticky="ns")
        
        # Refresh transactions button
        ttk.Button(history_frame, text="🔄 Refresh History", 
                  command=self.refresh_transaction_history).grid(row=1, column=0, pady=5)
    
    def create_statistics_panel(self, parent):
        """Create statistics panel"""
        stats_frame = ttk.LabelFrame(parent, text="📈 Real-time Statistics", 
                                   style='Card.TFrame', padding="10")
        stats_frame.grid(row=2, column=0, columnspan=3, sticky="we", 
                        pady=10)
        
        # Statistics display
        self.stats_text = tk.Text(stats_frame, height=6, wrap=tk.WORD, 
                                state=tk.DISABLED, font=('Arial', 10))
        self.stats_text.grid(row=0, column=0, sticky="we")
        
        # Auto-refresh stats
        self.refresh_statistics()
    
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
                messagebox.showerror("Error", f"Error loading data: {e}")
                self.create_default_accounts()
        else:
            self.create_default_accounts()
    
    def save_data(self):
        """Save banking data to JSON file"""
        try:
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
                
        except Exception as e:
            messagebox.showerror("Error", f"Error saving data: {e}")
    
    def create_default_accounts(self):
        """Create some default accounts for demo"""
        accounts_data = [
            (123456, "Filan", "Fisteku", 500.0),
            (789012, "John", "Doe", 1000.0),
            (345678, "Jane", "Smith", 750.0)
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
        self.save_data()
    
    # CRUD Operations
    def create_account(self):
        """Create a new bank account"""
        try:
            first_name = self.first_name_var.get().strip()
            last_name = self.last_name_var.get().strip()
            balance_str = self.balance_var.get().strip()
            
            if not first_name or not last_name:
                messagebox.showerror("Error", "Please enter both first and last name")
                return
            
            try:
                balance = float(balance_str)
                if balance < 0:
                    messagebox.showerror("Error", "Balance cannot be negative")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid balance amount")
                return
            
            # Generate new account number
            account_number = max(self.accounts.keys()) + 1 if self.accounts else 100000
            
            # Create account
            owner = BankAccountOwner(first_name, last_name)
            account = BankAccount(account_number, owner, balance)
            self.accounts[account_number] = account
            
            # Log and save
            self.log_transaction(account_number, "ACCOUNT_CREATED", balance)
            
            # Clear form
            self.first_name_var.set("")
            self.last_name_var.set("")
            self.balance_var.set("0.00")
            
            # Refresh displays
            self.refresh_account_list()
            self.refresh_statistics()
            
            messagebox.showinfo("Success", f"Account {account_number} created successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error creating account: {e}")
    
    def update_account(self):
        """Update selected account"""
        selection = self.account_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an account to update")
            return
        
        # Get selected account
        account_text = self.account_listbox.get(selection[0])
        account_number = int(account_text.split(" - ")[0])
        account = self.accounts[account_number]
        
        # Create update dialog
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Account")
        update_window.geometry("300x200")
        
        # Current values
        ttk.Label(update_window, text="First Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        first_var = tk.StringVar(value=account.account_owner.first_name)
        ttk.Entry(update_window, textvariable=first_var, width=20).grid(row=0, column=1, padx=10, pady=5)
        
        ttk.Label(update_window, text="Last Name:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        last_var = tk.StringVar(value=account.account_owner.last_name)
        ttk.Entry(update_window, textvariable=last_var, width=20).grid(row=1, column=1, padx=10, pady=5)
        
        def save_updates():
            try:
                new_first = first_var.get().strip()
                new_last = last_var.get().strip()
                
                if not new_first or not new_last:
                    messagebox.showerror("Error", "Please enter both first and last name")
                    return
                
                # Update account owner (create new owner object)
                new_owner = BankAccountOwner(new_first, new_last)
                # Create updated account
                updated_account = BankAccount(account.account_number, new_owner, account.account_balance)
                self.accounts[account_number] = updated_account
                
                self.save_data()
                self.refresh_account_list()
                self.refresh_statistics()
                
                update_window.destroy()
                messagebox.showinfo("Success", "Account updated successfully!")
                
            except Exception as e:
                messagebox.showerror("Error", f"Error updating account: {e}")
        
        ttk.Button(update_window, text="💾 Save Updates", 
                  command=save_updates).grid(row=2, column=0, columnspan=2, pady=20)
    
    def delete_account(self):
        """Delete selected account"""
        selection = self.account_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an account to delete")
            return
        
        # Get selected account
        account_text = self.account_listbox.get(selection[0])
        account_number = int(account_text.split(" - ")[0])
        account = self.accounts[account_number]
        
        # Confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion", 
                                    f"Are you sure you want to delete account {account_number}?\n"
                                    f"Owner: {account.account_owner.full_name}\n"
                                    f"Balance: ${account.account_balance:.2f}")
        
        if confirm:
            del self.accounts[account_number]
            self.log_transaction(account_number, "ACCOUNT_DELETED", 0)
            self.refresh_account_list()
            self.refresh_statistics()
            self.clear_account_details()
            messagebox.showinfo("Success", "Account deleted successfully!")
    
    def refresh_account_list(self):
        """Refresh the account listbox"""
        self.account_listbox.delete(0, tk.END)
        
        for account in sorted(self.accounts.values(), key=lambda x: x.account_number):
            display_text = f"{account.account_number} - {account.account_owner.full_name} (${account.account_balance:.2f})"
            self.account_listbox.insert(tk.END, display_text)
        
        # Update comboboxes for transfer
        account_list = [f"{acc.account_number} - {acc.account_owner.full_name}" 
                       for acc in self.accounts.values()]
        self.from_account_combo['values'] = account_list
        self.to_account_combo['values'] = account_list
    
    def on_account_select(self, event):
        """Handle account selection"""
        selection = self.account_listbox.curselection()
        if not selection:
            return
        
        # Get selected account
        account_text = self.account_listbox.get(selection[0])
        account_number = int(account_text.split(" - ")[0])
        account = self.accounts[account_number]
        
        # Display account details
        self.display_account_details(account)
    
    def display_account_details(self, account):
        """Display detailed account information"""
        self.account_info_text.config(state=tk.NORMAL)
        self.account_info_text.delete(1.0, tk.END)
        
        # Account card format
        info = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                               ACCOUNT DETAILS                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  👤 Account Holder: {account.account_owner.full_name:<48} ║
║  🔢 Account Number: {account.account_number:<48} ║
║  💰 Current Balance: ${account.account_balance:<47.2f} ║
║                                                                              ║
║  📅 Status: Active                                                           ║
║  ⭐ Type: Premium Banking Account                                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📊 ACCOUNT STATISTICS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
        
        # Add transaction statistics for this account
        account_transactions = [t for t in self.transaction_history 
                              if t['account_number'] == account.account_number]
        
        if account_transactions:
            deposits = sum(t['amount'] for t in account_transactions 
                         if t['type'] == 'DEPOSIT' and t['success'])
            withdrawals = sum(t['amount'] for t in account_transactions 
                            if t['type'] == 'WITHDRAW' and t['success'])
            
            info += f"💵 Total Deposits: ${deposits:,.2f}\n"
            info += f"💸 Total Withdrawals: ${withdrawals:,.2f}\n"
            info += f"🔄 Net Activity: ${deposits - withdrawals:,.2f}\n"
            info += f"📊 Transaction Count: {len(account_transactions)}\n"
        else:
            info += "📝 No transaction history available\n"
        
        self.account_info_text.insert(1.0, info)
        self.account_info_text.config(state=tk.DISABLED)
    
    def clear_account_details(self):
        """Clear account details display"""
        self.account_info_text.config(state=tk.NORMAL)
        self.account_info_text.delete(1.0, tk.END)
        self.account_info_text.config(state=tk.DISABLED)
    
    def quick_deposit(self):
        """Quick deposit to selected account"""
        selection = self.account_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an account")
            return
        
        try:
            amount = float(self.operation_amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            # Get selected account
            account_text = self.account_listbox.get(selection[0])
            account_number = int(account_text.split(" - ")[0])
            account = self.accounts[account_number]
            
            # Perform deposit
            account.deposit(amount)
            self.log_transaction(account_number, "DEPOSIT", amount)
            
            # Refresh displays
            self.refresh_account_list()
            self.display_account_details(account)
            self.refresh_statistics()
            self.operation_amount_var.set("")
            
            messagebox.showinfo("Success", f"${amount:.2f} deposited successfully!")
            
        except ValueError as e:
            if "positive" in str(e):
                messagebox.showerror("Error", "Deposit amount must be positive")
            else:
                messagebox.showerror("Error", "Please enter a valid amount")
        except Exception as e:
            messagebox.showerror("Error", f"Error processing deposit: {e}")
    
    def quick_withdraw(self):
        """Quick withdrawal from selected account"""
        selection = self.account_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an account")
            return
        
        # Initialize variables to avoid unbound errors
        account_number = None
        amount = None
        
        try:
            amount = float(self.operation_amount_var.get())
            if amount <= 0:
                messagebox.showerror("Error", "Amount must be positive")
                return
            
            # Get selected account
            account_text = self.account_listbox.get(selection[0])
            account_number = int(account_text.split(" - ")[0])
            account = self.accounts[account_number]
            
            # Perform withdrawal
            account.withdraw(amount)
            self.log_transaction(account_number, "WITHDRAW", amount)
            
            # Refresh displays
            self.refresh_account_list()
            self.display_account_details(account)
            self.refresh_statistics()
            self.operation_amount_var.set("")
            
            messagebox.showinfo("Success", f"${amount:.2f} withdrawn successfully!")
            
        except ValueError as e:
            if "Insufficient balance" in str(e):
                messagebox.showerror("Error", "Insufficient balance for this withdrawal")
                if account_number is not None and amount is not None:
                    self.log_transaction(account_number, "WITHDRAW_FAILED", amount, False, str(e))
            elif "positive" in str(e):
                messagebox.showerror("Error", "Withdrawal amount must be positive")
            else:
                messagebox.showerror("Error", "Please enter a valid amount")
        except Exception as e:
            messagebox.showerror("Error", f"Error processing withdrawal: {e}")
    
    def transfer_money(self):
        """Transfer money between accounts"""
        # Initialize variables to avoid unbound errors
        from_acc_num = None
        amount = None
        
        try:
            from_text = self.from_account_var.get()
            to_text = self.to_account_var.get()
            amount = float(self.transfer_amount_var.get())
            
            if not from_text or not to_text:
                messagebox.showerror("Error", "Please select both source and destination accounts")
                return
            
            if amount <= 0:
                messagebox.showerror("Error", "Transfer amount must be positive")
                return
            
            # Extract account numbers
            from_acc_num = int(from_text.split(" - ")[0])
            to_acc_num = int(to_text.split(" - ")[0])
            
            if from_acc_num == to_acc_num:
                messagebox.showerror("Error", "Cannot transfer to the same account")
                return
            
            # Get accounts
            from_account = self.accounts[from_acc_num]
            to_account = self.accounts[to_acc_num]
            
            # Perform transfer
            from_account.withdraw(amount)
            to_account.deposit(amount)
            
            # Log transactions
            self.log_transaction(from_acc_num, "TRANSFER_OUT", amount)
            self.log_transaction(to_acc_num, "TRANSFER_IN", amount)
            
            # Refresh displays
            self.refresh_account_list()
            self.refresh_statistics()
            self.refresh_transaction_history()
            self.transfer_amount_var.set("")
            
            messagebox.showinfo("Success", 
                              f"${amount:.2f} transferred successfully!\n"
                              f"From: {from_account.account_owner.full_name}\n"
                              f"To: {to_account.account_owner.full_name}")
            
        except ValueError as e:
            if "Insufficient balance" in str(e):
                messagebox.showerror("Error", "Insufficient balance for transfer")
                if from_acc_num is not None and amount is not None:
                    self.log_transaction(from_acc_num, "TRANSFER_FAILED", amount, False, str(e))
            else:
                messagebox.showerror("Error", "Please enter a valid transfer amount")
        except Exception as e:
            messagebox.showerror("Error", f"Error processing transfer: {e}")
    
    def refresh_transaction_history(self):
        """Refresh transaction history display"""
        # Clear existing items
        for item in self.transaction_tree.get_children():
            self.transaction_tree.delete(item)
        
        # Add recent transactions (last 20)
        recent_transactions = self.transaction_history[-20:]
        
        for trans in reversed(recent_transactions):
            timestamp = trans['timestamp'][:19].replace('T', ' ')
            account_num = trans['account_number']
            trans_type = trans['type']
            amount = f"${trans['amount']:.2f}" if trans['amount'] else "N/A"
            status = "✅" if trans['success'] else "❌"
            
            self.transaction_tree.insert("", "end", values=(timestamp, account_num, 
                                                          trans_type, amount, status))
    
    def refresh_statistics(self):
        """Refresh statistics display"""
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        
        # Calculate statistics
        total_accounts = len(self.accounts)
        total_balance = sum(acc.account_balance for acc in self.accounts.values())
        avg_balance = total_balance / max(total_accounts, 1)
        
        total_transactions = len(self.transaction_history)
        successful_transactions = sum(1 for t in self.transaction_history if t['success'])
        success_rate = (successful_transactions / max(total_transactions, 1)) * 100
        
        stats_text = f"""
📊 REAL-TIME BANKING STATISTICS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💼 PORTFOLIO OVERVIEW:  👥 Total Accounts: {total_accounts}  |  💰 Total Assets: ${total_balance:,.2f}  |  📊 Average Balance: ${avg_balance:,.2f}

📈 TRANSACTION METRICS:  🔄 Total Transactions: {total_transactions}  |  ✅ Success Rate: {success_rate:.1f}%  |  📅 Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        self.stats_text.insert(1.0, stats_text)
        self.stats_text.config(state=tk.DISABLED)
        
        # Schedule next refresh
        self.root.after(5000, self.refresh_statistics)  # Refresh every 5 seconds

def main():
    """Main application entry point"""
    root = tk.Tk()
    app = ProfessionalBankingGUI(root)
    
    # Load transaction history on startup
    app.refresh_transaction_history()
    
    root.mainloop()

if __name__ == "__main__":
    main()
