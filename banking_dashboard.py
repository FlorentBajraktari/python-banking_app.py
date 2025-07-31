# banking_dashboard.py - Interactive Statistics Dashboard

import json
import datetime
from collections import defaultdict
import os

class BankingDashboard:
    def __init__(self, data_file="banking_data.json"):
        self.data_file = data_file
        self.load_data()
    
    def load_data(self):
        """Load banking data for analysis"""
        self.accounts = {}
        self.transaction_history = []
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                self.accounts = data.get('accounts', {})
                self.transaction_history = data.get('transaction_history', [])
            except:
                pass
    
    def get_total_assets(self):
        """Calculate total assets across all accounts"""
        return sum(acc['balance'] for acc in self.accounts.values())
    
    def get_account_count(self):
        """Get total number of accounts"""
        return len(self.accounts)
    
    def get_transaction_stats(self):
        """Get transaction statistics"""
        if not self.transaction_history:
            return {}
        
        stats = {
            'total_transactions': len(self.transaction_history),
            'successful_transactions': 0,
            'failed_transactions': 0,
            'total_deposits': 0,
            'total_withdrawals': 0,
            'total_transfers': 0
        }
        
        for trans in self.transaction_history:
            if trans['success']:
                stats['successful_transactions'] += 1
                if trans['type'] == 'DEPOSIT':
                    stats['total_deposits'] += trans['amount']
                elif trans['type'] == 'WITHDRAW':
                    stats['total_withdrawals'] += trans['amount']
                elif 'TRANSFER' in trans['type']:
                    stats['total_transfers'] += trans['amount']
            else:
                stats['failed_transactions'] += 1
        
        return stats
    
    def get_daily_activity(self):
        """Get daily transaction activity"""
        daily_stats = defaultdict(int)
        
        for trans in self.transaction_history:
            date = trans['timestamp'][:10]  # Extract date part
            daily_stats[date] += 1
        
        return dict(daily_stats)
    
    def get_top_accounts_by_balance(self, top_n=5):
        """Get top accounts by balance"""
        accounts_list = [
            (acc_num, acc_data['owner_first_name'] + ' ' + acc_data['owner_last_name'], acc_data['balance'])
            for acc_num, acc_data in self.accounts.items()
        ]
        
        return sorted(accounts_list, key=lambda x: x[2], reverse=True)[:top_n]
    
    def print_dashboard(self):
        """Print the main dashboard"""
        print("\n" + "="*80)
        print("📊 BANKING ANALYTICS DASHBOARD 📊")
        print("="*80)
        
        # Basic Stats
        total_assets = self.get_total_assets()
        account_count = self.get_account_count()
        
        print(f"\n💼 PORTFOLIO OVERVIEW:")
        print(f"   💰 Total Assets: ${total_assets:,.2f}")
        print(f"   👥 Total Accounts: {account_count}")
        print(f"   📊 Average Balance: ${total_assets/max(account_count, 1):,.2f}")
        
        # Transaction Stats
        trans_stats = self.get_transaction_stats()
        if trans_stats:
            success_rate = (trans_stats['successful_transactions'] / trans_stats['total_transactions']) * 100
            
            print(f"\n📈 TRANSACTION ANALYTICS:")
            print(f"   🔄 Total Transactions: {trans_stats['total_transactions']}")
            print(f"   ✅ Success Rate: {success_rate:.1f}%")
            print(f"   💵 Total Deposits: ${trans_stats['total_deposits']:,.2f}")
            print(f"   💸 Total Withdrawals: ${trans_stats['total_withdrawals']:,.2f}")
            print(f"   🔄 Transfer Volume: ${trans_stats['total_transfers']:,.2f}")
        
        # Top Accounts
        top_accounts = self.get_top_accounts_by_balance()
        if top_accounts:
            print(f"\n🏆 TOP ACCOUNTS BY BALANCE:")
            for i, (acc_num, owner, balance) in enumerate(top_accounts, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
                print(f"   {medal} {acc_num} - {owner}: ${balance:,.2f}")
        
        # Daily Activity (last 7 days)
        daily_activity = self.get_daily_activity()
        if daily_activity:
            print(f"\n📅 RECENT ACTIVITY (Last 7 days):")
            sorted_days = sorted(daily_activity.items(), reverse=True)[:7]
            for date, count in sorted_days:
                bar = "█" * min(count, 20)
                print(f"   {date}: {bar} ({count} transactions)")
        
        print("="*80)
    
    def print_account_analysis(self, account_number):
        """Print detailed analysis for a specific account"""
        if str(account_number) not in self.accounts:
            print(f"❌ Account {account_number} not found")
            return
        
        account = self.accounts[str(account_number)]
        
        print(f"\n📊 ACCOUNT ANALYSIS - {account_number}")
        print("="*60)
        print(f"👤 Owner: {account['owner_first_name']} {account['owner_last_name']}")
        print(f"💰 Current Balance: ${account['balance']:,.2f}")
        
        # Transaction history for this account
        account_transactions = [
            t for t in self.transaction_history 
            if t['account_number'] == account_number
        ]
        
        if account_transactions:
            deposits = sum(t['amount'] for t in account_transactions if t['type'] == 'DEPOSIT' and t['success'])
            withdrawals = sum(t['amount'] for t in account_transactions if t['type'] == 'WITHDRAW' and t['success'])
            
            print(f"📈 Total Deposits: ${deposits:,.2f}")
            print(f"📉 Total Withdrawals: ${withdrawals:,.2f}")
            print(f"🔄 Net Activity: ${deposits - withdrawals:,.2f}")
            print(f"📊 Transaction Count: {len(account_transactions)}")
        
        print("="*60)
    
    def export_report(self):
        """Export dashboard data to a text file"""
        report_file = f"banking_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        with open(report_file, 'w') as f:
            f.write("BANKING ANALYTICS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Basic stats
            total_assets = self.get_total_assets()
            account_count = self.get_account_count()
            
            f.write("PORTFOLIO OVERVIEW:\n")
            f.write(f"Total Assets: ${total_assets:,.2f}\n")
            f.write(f"Total Accounts: {account_count}\n")
            f.write(f"Average Balance: ${total_assets/max(account_count, 1):,.2f}\n\n")
            
            # Top accounts
            top_accounts = self.get_top_accounts_by_balance()
            f.write("TOP ACCOUNTS:\n")
            for i, (acc_num, owner, balance) in enumerate(top_accounts, 1):
                f.write(f"{i}. {acc_num} - {owner}: ${balance:,.2f}\n")
            
        print(f"📄 Report exported to: {report_file}")

def main():
    """Main dashboard application"""
    dashboard = BankingDashboard()
    
    while True:
        print("\n🎯 BANKING ANALYTICS MENU")
        print("1. 📊 View Dashboard")
        print("2. 🔍 Analyze Specific Account")
        print("3. 📄 Export Report")
        print("4. 🔙 Back to Main System")
        
        choice = input("\nChoose option (1-4): ").strip()
        
        if choice == '1':
            dashboard.print_dashboard()
        elif choice == '2':
            try:
                acc_num = int(input("Enter account number: "))
                dashboard.print_account_analysis(acc_num)
            except ValueError:
                print("❌ Invalid account number")
        elif choice == '3':
            dashboard.export_report()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
