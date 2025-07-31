# Enhanced_Professional_GUI.py - Ultra-Modern Banking Interface

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
import datetime
from Model import BankAccount, BankAccountOwner, TransactionType

class EnhancedProfessionalBankingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏦 Elite Banking System - Professional Interface")
        self.root.geometry("1400x900")
        self.root.configure(bg='#2c3e50')
        
        # Data storage
        self.data_file = "banking_data.json"
        self.accounts = {}
        self.transaction_history = []
        self.selected_account = None
        
        # Load existing data
        self.load_data()
        
        # Configure modern styles
        self.setup_modern_styles()
        
        # Create main interface
        self.create_modern_interface()
        
        # Load initial data
        self.refresh_all_displays()
        
    def setup_modern_styles(self):
        """Setup ultra-modern styles for professional look"""
        style = ttk.Style()
        
        # Set theme
        try:
            style.theme_use('clam')
        except:
            pass
        
        # Define color palette
        self.colors = {
            'primary': '#3498db',      # Blue
            'secondary': '#2ecc71',    # Green
            'danger': '#e74c3c',       # Red
            'warning': '#f39c12',      # Orange
            'dark': '#2c3e50',         # Dark blue
            'light': '#ecf0f1',        # Light gray
            'white': '#ffffff',
            'text': '#2c3e50'
        }
        
        # Configure modern button styles
        style.configure('Modern.TButton', 
                       font=('Segoe UI', 10, 'bold'),
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        style.configure('Primary.TButton',
                       font=('Segoe UI', 11, 'bold'),
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none')
        
        style.configure('Success.TButton',
                       font=('Segoe UI', 10),
                       foreground='white',
                       borderwidth=0)
        
        style.configure('Danger.TButton',
                       font=('Segoe UI', 10),
                       foreground='white',
                       borderwidth=0)
        
        # Configure frame styles
        style.configure('Card.TFrame',
                       relief='flat',
                       borderwidth=1,
                       background='white')
        
        style.configure('Header.TFrame',
                       relief='flat',
                       background=self.colors['primary'])
        
        # Configure label styles
        style.configure('Title.TLabel',
                       font=('Segoe UI', 24, 'bold'),
                       foreground='white',
                       background=self.colors['primary'])
        
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 14, 'bold'),
                       foreground=self.colors['text'],
                       background='white')
        
        style.configure('CardTitle.TLabel',
                       font=('Segoe UI', 12, 'bold'),
                       foreground=self.colors['text'],
                       background='white')
        
        style.configure('Info.TLabel',
                       font=('Segoe UI', 10),
                       foreground=self.colors['text'],
                       background='white')
        
        # Configure entry styles
        style.configure('Modern.TEntry',
                       font=('Segoe UI', 10),
                       fieldbackground='white',
                       borderwidth=1,
                       relief='solid')
    
    def create_modern_interface(self):
        """Create the ultra-modern GUI interface"""
        # Main container with modern styling
        main_container = tk.Frame(self.root, bg=self.colors['light'])
        main_container.pack(fill='both', expand=True)
        
        # Header section
        self.create_header_section(main_container)
        
        # Content area with cards
        content_frame = tk.Frame(main_container, bg=self.colors['light'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create three-column layout
        self.create_account_card(content_frame)
        self.create_transaction_card(content_frame)
        self.create_dashboard_card(content_frame)
        
        # Footer with statistics
        self.create_footer_section(main_container)
    
    def create_header_section(self, parent):
        """Create modern header with gradient-like appearance"""
        header_frame = tk.Frame(parent, bg=self.colors['primary'], height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Title with modern typography
        title_label = tk.Label(header_frame, 
                              text="🏦 Elite Banking System", 
                              font=('Segoe UI', 28, 'bold'),
                              fg='white',
                              bg=self.colors['primary'])
        title_label.pack(pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame,
                                 text="Professional Account Management & Transaction Platform",
                                 font=('Segoe UI', 12),
                                 fg='white',
                                 bg=self.colors['primary'])
        subtitle_label.pack()
    
    def create_account_card(self, parent):
        """Create modern account management card"""
        # Card container
        card_frame = tk.Frame(parent, bg='white', relief='solid', bd=1)
        card_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10), pady=10)
        
        # Card header
        header = tk.Frame(card_frame, bg=self.colors['secondary'], height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        header_label = tk.Label(header, 
                               text="👥 Account Management",
                               font=('Segoe UI', 14, 'bold'),
                               fg='white',
                               bg=self.colors['secondary'])
        header_label.pack(pady=12)
        
        # Card content
        content = tk.Frame(card_frame, bg='white', padx=20, pady=20)
        content.pack(fill='both', expand=True)
        
        # Account List
        list_frame = tk.LabelFrame(content, text="📋 Accounts", 
                                  font=('Segoe UI', 10, 'bold'),
                                  bg='white', fg=self.colors['text'])
        list_frame.pack(fill='both', expand=True, pady=(0, 15))
        
        # Account Listbox with modern styling
        self.account_listbox = tk.Listbox(list_frame, 
                                         font=('Segoe UI', 10),
                                         bg='#f8f9fa',
                                         selectbackground=self.colors['primary'],
                                         selectforeground='white',
                                         borderwidth=0,
                                         highlightthickness=1,
                                         highlightcolor=self.colors['primary'])
        self.account_listbox.pack(fill='both', expand=True, padx=10, pady=10)
        self.account_listbox.bind('<<ListboxSelect>>', self.on_account_select)
        
        # Create Account Section
        create_frame = tk.LabelFrame(content, text="➕ Create New Account",
                                   font=('Segoe UI', 10, 'bold'),
                                   bg='white', fg=self.colors['text'])
        create_frame.pack(fill='x', pady=(0, 15))
        
        # Input fields with modern styling
        input_frame = tk.Frame(create_frame, bg='white', padx=15, pady=15)
        input_frame.pack(fill='x')
        
        # First Name
        tk.Label(input_frame, text="First Name:", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=0, column=0, sticky='w', pady=2)
        self.first_name_var = tk.StringVar()
        first_entry = tk.Entry(input_frame, textvariable=self.first_name_var,
                              font=('Segoe UI', 10), width=20,
                              relief='solid', bd=1)
        first_entry.grid(row=0, column=1, pady=2, padx=(10, 0))
        
        # Last Name
        tk.Label(input_frame, text="Last Name:", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=1, column=0, sticky='w', pady=2)
        self.last_name_var = tk.StringVar()
        last_entry = tk.Entry(input_frame, textvariable=self.last_name_var,
                             font=('Segoe UI', 10), width=20,
                             relief='solid', bd=1)
        last_entry.grid(row=1, column=1, pady=2, padx=(10, 0))
        
        # Initial Deposit
        tk.Label(input_frame, text="Initial Deposit:", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=2, column=0, sticky='w', pady=2)
        self.balance_var = tk.StringVar(value="0.00")
        balance_entry = tk.Entry(input_frame, textvariable=self.balance_var,
                               font=('Segoe UI', 10), width=20,
                               relief='solid', bd=1)
        balance_entry.grid(row=2, column=1, pady=2, padx=(10, 0))
        
        # Create button
        create_btn = tk.Button(input_frame, text="✨ Create Account",
                              command=self.create_account,
                              font=('Segoe UI', 10, 'bold'),
                              bg=self.colors['secondary'],
                              fg='white',
                              relief='flat',
                              padx=20, pady=8)
        create_btn.grid(row=3, column=0, columnspan=2, pady=15)
        
        # Account Actions
        actions_frame = tk.LabelFrame(content, text="⚡ Account Actions",
                                    font=('Segoe UI', 10, 'bold'),
                                    bg='white', fg=self.colors['text'])
        actions_frame.pack(fill='x')
        
        action_buttons = tk.Frame(actions_frame, bg='white', padx=15, pady=15)
        action_buttons.pack()
        
        # Modern action buttons
        deposit_btn = tk.Button(action_buttons, text="💰 Deposit",
                               command=self.quick_deposit,
                               font=('Segoe UI', 9, 'bold'),
                               bg=self.colors['secondary'],
                               fg='white',
                               relief='flat',
                               padx=15, pady=6)
        deposit_btn.grid(row=0, column=0, padx=5)
        
        withdraw_btn = tk.Button(action_buttons, text="💸 Withdraw",
                                command=self.quick_withdraw,
                                font=('Segoe UI', 9, 'bold'),
                                bg=self.colors['danger'],
                                fg='white',
                                relief='flat',
                                padx=15, pady=6)
        withdraw_btn.grid(row=0, column=1, padx=5)
        
        delete_btn = tk.Button(action_buttons, text="🗑️ Delete",
                              command=self.delete_account,
                              font=('Segoe UI', 9, 'bold'),
                              bg=self.colors['warning'],
                              fg='white',
                              relief='flat',
                              padx=15, pady=6)
        delete_btn.grid(row=0, column=2, padx=5)
        
        parent.columnconfigure(0, weight=1)
    
    def create_transaction_card(self, parent):
        """Create modern transaction card"""
        # Card container
        card_frame = tk.Frame(parent, bg='white', relief='solid', bd=1)
        card_frame.grid(row=0, column=1, sticky='nsew', padx=5, pady=10)
        
        # Card header
        header = tk.Frame(card_frame, bg=self.colors['warning'], height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        header_label = tk.Label(header, 
                               text="🔄 Transactions",
                               font=('Segoe UI', 14, 'bold'),
                               fg='white',
                               bg=self.colors['warning'])
        header_label.pack(pady=12)
        
        # Card content
        content = tk.Frame(card_frame, bg='white', padx=20, pady=20)
        content.pack(fill='both', expand=True)
        
        # Transfer Section
        transfer_frame = tk.LabelFrame(content, text="💸 Transfer Money",
                                     font=('Segoe UI', 10, 'bold'),
                                     bg='white', fg=self.colors['text'])
        transfer_frame.pack(fill='x', pady=(0, 15))
        
        transfer_content = tk.Frame(transfer_frame, bg='white', padx=15, pady=15)
        transfer_content.pack(fill='x')
        
        # From Account
        tk.Label(transfer_content, text="From Account:", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=0, column=0, sticky='w', pady=5)
        self.from_account_var = tk.StringVar()
        from_combo = ttk.Combobox(transfer_content, textvariable=self.from_account_var,
                                 font=('Segoe UI', 9), width=25, state="readonly")
        from_combo.grid(row=0, column=1, pady=5, padx=(10, 0), sticky='w')
        self.from_account_combo = from_combo
        
        # To Account
        tk.Label(transfer_content, text="To Account:", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=1, column=0, sticky='w', pady=5)
        self.to_account_var = tk.StringVar()
        to_combo = ttk.Combobox(transfer_content, textvariable=self.to_account_var,
                               font=('Segoe UI', 9), width=25, state="readonly")
        to_combo.grid(row=1, column=1, pady=5, padx=(10, 0), sticky='w')
        self.to_account_combo = to_combo
        
        # Transfer Amount
        tk.Label(transfer_content, text="Amount ($):", 
                font=('Segoe UI', 9), bg='white', fg=self.colors['text']).grid(row=2, column=0, sticky='w', pady=5)
        self.transfer_amount_var = tk.StringVar()
        amount_entry = tk.Entry(transfer_content, textvariable=self.transfer_amount_var,
                               font=('Segoe UI', 10), width=27, relief='solid', bd=1)
        amount_entry.grid(row=2, column=1, pady=5, padx=(10, 0), sticky='w')
        
        # Transfer button
        transfer_btn = tk.Button(transfer_content, text="🚀 Execute Transfer",
                                command=self.transfer_money,
                                font=('Segoe UI', 10, 'bold'),
                                bg=self.colors['primary'],
                                fg='white',
                                relief='flat',
                                padx=20, pady=8)
        transfer_btn.grid(row=3, column=0, columnspan=2, pady=15)
        
        # Transaction History
        history_frame = tk.LabelFrame(content, text="📜 Transaction History",
                                    font=('Segoe UI', 10, 'bold'),
                                    bg='white', fg=self.colors['text'])
        history_frame.pack(fill='both', expand=True)
        
        # Modern Treeview
        tree_frame = tk.Frame(history_frame, bg='white')
        tree_frame.pack(fill='both', expand=True, padx=15, pady=15)
        
        columns = ("Time", "Account", "Type", "Amount", "Status")
        self.transaction_tree = ttk.Treeview(tree_frame, columns=columns,
                                           show="headings", height=10)
        
        # Configure columns with modern styling
        for col in columns:
            self.transaction_tree.heading(col, text=col)
            self.transaction_tree.column(col, width=100, anchor='center')
        
        # Scrollbar
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical",
                                  command=self.transaction_tree.yview)
        self.transaction_tree.configure(yscrollcommand=tree_scroll.set)
        
        self.transaction_tree.pack(side='left', fill='both', expand=True)
        tree_scroll.pack(side='right', fill='y')
        
        # Refresh button
        refresh_btn = tk.Button(history_frame, text="🔄 Refresh History",
                               command=self.refresh_transaction_history,
                               font=('Segoe UI', 9),
                               bg=self.colors['light'],
                               fg=self.colors['text'],
                               relief='flat',
                               padx=15, pady=5)
        refresh_btn.pack(pady=10)
        
        parent.columnconfigure(1, weight=1)
    
    def create_dashboard_card(self, parent):
        """Create modern dashboard card"""
        # Card container
        card_frame = tk.Frame(parent, bg='white', relief='solid', bd=1)
        card_frame.grid(row=0, column=2, sticky='nsew', padx=(10, 0), pady=10)
        
        # Card header
        header = tk.Frame(card_frame, bg=self.colors['danger'], height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        header_label = tk.Label(header, 
                               text="📊 Dashboard",
                               font=('Segoe UI', 14, 'bold'),
                               fg='white',
                               bg=self.colors['danger'])
        header_label.pack(pady=12)
        
        # Card content
        content = tk.Frame(card_frame, bg='white', padx=20, pady=20)
        content.pack(fill='both', expand=True)
        
        # Account Details
        details_frame = tk.LabelFrame(content, text="🔍 Account Details",
                                    font=('Segoe UI', 10, 'bold'),
                                    bg='white', fg=self.colors['text'])
        details_frame.pack(fill='x', pady=(0, 15))
        
        # Details display
        self.details_text = tk.Text(details_frame, height=8, wrap=tk.WORD,
                                   font=('Segoe UI', 9),
                                   bg='#f8f9fa',
                                   fg=self.colors['text'],
                                   state=tk.DISABLED,
                                   relief='flat',
                                   borderwidth=1)
        self.details_text.pack(fill='x', padx=15, pady=15)
        
        # Statistics
        stats_frame = tk.LabelFrame(content, text="📈 Real-time Statistics",
                                  font=('Segoe UI', 10, 'bold'),
                                  bg='white', fg=self.colors['text'])
        stats_frame.pack(fill='both', expand=True)
        
        # Statistics display
        self.stats_text = tk.Text(stats_frame, height=8, wrap=tk.WORD,
                                 font=('Segoe UI', 9),
                                 bg='#f8f9fa',
                                 fg=self.colors['text'],
                                 state=tk.DISABLED,
                                 relief='flat',
                                 borderwidth=1)
        self.stats_text.pack(fill='both', expand=True, padx=15, pady=15)
        
        parent.columnconfigure(2, weight=1)
    
    def create_footer_section(self, parent):
        """Create modern footer with status information"""
        footer_frame = tk.Frame(parent, bg=self.colors['dark'], height=40)
        footer_frame.pack(fill='x')
        footer_frame.pack_propagate(False)
        
        # Status label
        status_text = f"💾 Data file: {self.data_file} | 📊 Accounts: {len(self.accounts)} | 🕒 {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        status_label = tk.Label(footer_frame,
                               text=status_text,
                               font=('Segoe UI', 9),
                               fg='white',
                               bg=self.colors['dark'])
        status_label.pack(pady=10)
    
    # Data Management Methods
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
            (345678, "Jane", "Smith", 750.0),
            (901234, "Alice", "Johnson", 1250.0),
            (567890, "Bob", "Wilson", 850.0)
        ]
        
        for acc_num, first, last, balance in accounts_data:
            owner = BankAccountOwner(first, last)
            account = BankAccount(acc_num, owner, balance)
            self.accounts[acc_num] = account
    
    def log_transaction(self, account_number, transaction_type, amount, success=True, error_msg=""):
        """Log transaction for history"""
        transaction = {
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
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
            self.refresh_all_displays()
            
            messagebox.showinfo("Success", f"✅ Account {account_number} created successfully!\n\n👤 Owner: {first_name} {last_name}\n💰 Initial Balance: ${balance:.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error creating account: {e}")
    
    def delete_account(self):
        """Delete selected account"""
        if not self.selected_account:
            messagebox.showwarning("Warning", "Please select an account to delete")
            return
        
        account = self.accounts[self.selected_account]
        
        if messagebox.askyesno("Confirm Delete", 
                              f"Are you sure you want to delete account {self.selected_account}?\n\nOwner: {account.account_owner.full_name}\nBalance: ${account.account_balance:.2f}\n\nThis action cannot be undone!"):
            
            # Log transaction
            self.log_transaction(self.selected_account, "ACCOUNT_DELETED", account.account_balance)
            
            # Delete account
            del self.accounts[self.selected_account]
            self.selected_account = None
            
            # Refresh displays
            self.refresh_all_displays()
            
            messagebox.showinfo("Success", "Account deleted successfully!")
    
    def quick_deposit(self):
        """Quick deposit to selected account"""
        if not self.selected_account:
            messagebox.showwarning("Warning", "Please select an account first")
            return
        
        amount_str = simpledialog.askstring("Deposit", "Enter deposit amount:")
        if amount_str:
            try:
                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive")
                    return
                
                account = self.accounts[self.selected_account]
                account.deposit(amount)
                
                self.log_transaction(self.selected_account, "DEPOSIT", amount)
                self.refresh_all_displays()
                
                messagebox.showinfo("Success", f"✅ ${amount:.2f} deposited successfully!\n\nNew Balance: ${account.account_balance:.2f}")
                
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def quick_withdraw(self):
        """Quick withdrawal from selected account"""
        if not self.selected_account:
            messagebox.showwarning("Warning", "Please select an account first")
            return
        
        amount_str = simpledialog.askstring("Withdraw", "Enter withdrawal amount:")
        if amount_str:
            amount = None
            try:
                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive")
                    return
                
                account = self.accounts[self.selected_account]
                account.withdraw(amount)
                
                self.log_transaction(self.selected_account, "WITHDRAWAL", amount)
                self.refresh_all_displays()
                
                messagebox.showinfo("Success", f"✅ ${amount:.2f} withdrawn successfully!\n\nNew Balance: ${account.account_balance:.2f}")
                
            except ValueError as ve:
                if "Insufficient balance" in str(ve) and amount is not None:
                    messagebox.showerror("Error", "Insufficient balance for this withdrawal")
                    self.log_transaction(self.selected_account, "WITHDRAWAL_FAILED", amount, False, str(ve))
                else:
                    messagebox.showerror("Error", "Please enter a valid amount")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def transfer_money(self):
        """Transfer money between accounts"""
        from_acc = None
        amount = None
        
        try:
            from_acc_str = self.from_account_var.get()
            to_acc_str = self.to_account_var.get()
            amount_str = self.transfer_amount_var.get().strip()
            
            if not from_acc_str or not to_acc_str:
                messagebox.showerror("Error", "Please select both accounts")
                return
            
            from_acc = int(from_acc_str.split(' - ')[0])
            to_acc = int(to_acc_str.split(' - ')[0])
            
            if from_acc == to_acc:
                messagebox.showerror("Error", "Cannot transfer to the same account")
                return
            
            try:
                amount = float(amount_str)
                if amount <= 0:
                    messagebox.showerror("Error", "Amount must be positive")
                    return
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount")
                return
            
            # Perform transfer
            source_account = self.accounts[from_acc]
            dest_account = self.accounts[to_acc]
            
            source_account.withdraw(amount)
            dest_account.deposit(amount)
            
            self.log_transaction(from_acc, "TRANSFER_OUT", amount)
            self.log_transaction(to_acc, "TRANSFER_IN", amount)
            
            # Clear form
            self.transfer_amount_var.set("")
            
            # Refresh displays
            self.refresh_all_displays()
            
            messagebox.showinfo("Success", f"✅ Transfer completed successfully!\n\n💸 ${amount:.2f} transferred\n📤 From: {source_account.account_owner.full_name}\n📥 To: {dest_account.account_owner.full_name}\n\n📊 New Balances:\n💰 Source: ${source_account.account_balance:.2f}\n💰 Destination: ${dest_account.account_balance:.2f}")
            
        except ValueError as ve:
            if "Insufficient balance" in str(ve) and from_acc is not None and amount is not None:
                messagebox.showerror("Error", "Insufficient balance for transfer")
                self.log_transaction(from_acc, "TRANSFER_FAILED", amount, False, str(ve))
            else:
                messagebox.showerror("Error", f"Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Transfer failed: {e}")
    
    # UI Update Methods
    def refresh_all_displays(self):
        """Refresh all display elements"""
        self.refresh_account_list()
        self.refresh_account_combos()
        self.refresh_account_details()
        self.refresh_statistics()
        self.refresh_transaction_history()
    
    def refresh_account_list(self):
        """Refresh the account listbox"""
        self.account_listbox.delete(0, tk.END)
        for account in self.accounts.values():
            display_text = f"{account.account_number} - {account.account_owner.full_name} (${account.account_balance:.2f})"
            self.account_listbox.insert(tk.END, display_text)
    
    def refresh_account_combos(self):
        """Refresh account combo boxes for transfers"""
        account_list = []
        for account in self.accounts.values():
            display_text = f"{account.account_number} - {account.account_owner.full_name}"
            account_list.append(display_text)
        
        self.from_account_combo['values'] = account_list
        self.to_account_combo['values'] = account_list
    
    def refresh_account_details(self):
        """Refresh account details display"""
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)
        
        if self.selected_account and self.selected_account in self.accounts:
            account = self.accounts[self.selected_account]
            details = f"""🏦 ACCOUNT DETAILS
{'='*30}

📋 Account Number: {account.account_number}
👤 Owner: {account.account_owner.full_name}
💰 Current Balance: ${account.account_balance:.2f}
📅 Last Updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

💳 Account Status: {'🟢 Active' if account.account_balance >= 0 else '🔴 Overdrawn'}
🏆 Account Type: Premium Banking
🔒 Security Level: High"""
        else:
            details = """🔍 SELECT AN ACCOUNT
{'='*30}

👆 Click on an account from the list 
   to view detailed information.

📊 Account details will include:
   • Account number & owner
   • Current balance
   • Account status
   • Last update time"""
        
        self.details_text.insert(1.0, details)
        self.details_text.config(state=tk.DISABLED)
    
    def refresh_statistics(self):
        """Refresh statistics display"""
        self.stats_text.config(state=tk.NORMAL)
        self.stats_text.delete(1.0, tk.END)
        
        if self.accounts:
            total_balance = sum(acc.account_balance for acc in self.accounts.values())
            avg_balance = total_balance / len(self.accounts)
            max_balance = max(acc.account_balance for acc in self.accounts.values())
            min_balance = min(acc.account_balance for acc in self.accounts.values())
            
            # Recent transactions count
            today = datetime.datetime.now().date()
            today_transactions = sum(1 for t in self.transaction_history 
                                   if datetime.datetime.fromisoformat(t['timestamp'].replace('Z', '')).date() == today)
            
            stats = f"""📈 BANKING STATISTICS
{'='*30}

👥 Total Accounts: {len(self.accounts)}
💰 Total Balance: ${total_balance:.2f}
📊 Average Balance: ${avg_balance:.2f}
🔺 Highest Balance: ${max_balance:.2f}
🔻 Lowest Balance: ${min_balance:.2f}

📜 Total Transactions: {len(self.transaction_history)}
📅 Today's Transactions: {today_transactions}

🏆 Bank Performance: {'🟢 Excellent' if avg_balance > 500 else '🟡 Good' if avg_balance > 200 else '🔴 Needs Attention'}
💎 Premium Customers: {sum(1 for acc in self.accounts.values() if acc.account_balance > 1000)}"""
        else:
            stats = """📈 BANKING STATISTICS
{'='*30}

📊 No accounts available yet.

🚀 Create your first account to see:
   • Total balances
   • Account statistics  
   • Transaction metrics
   • Performance indicators"""
        
        self.stats_text.insert(1.0, stats)
        self.stats_text.config(state=tk.DISABLED)
    
    def refresh_transaction_history(self):
        """Refresh transaction history display"""
        # Clear existing items
        for item in self.transaction_tree.get_children():
            self.transaction_tree.delete(item)
        
        # Show last 20 transactions
        recent_transactions = self.transaction_history[-20:] if len(self.transaction_history) > 20 else self.transaction_history
        
        for transaction in reversed(recent_transactions):
            time_str = transaction['timestamp'][:16]  # Show only date and time
            account_num = transaction['account_number']
            trans_type = transaction['type']
            amount = f"${transaction['amount']:.2f}"
            status = "✅ Success" if transaction['success'] else "❌ Failed"
            
            self.transaction_tree.insert('', 0, values=(time_str, account_num, trans_type, amount, status))
    
    def on_account_select(self, event):
        """Handle account selection"""
        selection = self.account_listbox.curselection()
        if selection:
            index = selection[0]
            account_text = self.account_listbox.get(index)
            self.selected_account = int(account_text.split(' - ')[0])
            self.refresh_account_details()

def main():
    """Main function to run the Enhanced Professional Banking GUI"""
    root = tk.Tk()
    app = EnhancedProfessionalBankingGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
