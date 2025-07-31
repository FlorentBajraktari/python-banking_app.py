# banking_art.py - ASCII Art and Visual Enhancements

def print_welcome_banner():
    """Print a beautiful welcome banner"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    ██████╗  █████╗ ███╗   ██╗██╗  ██╗██╗███╗   ██╗ ██████╗                   ║
║    ██╔══██╗██╔══██╗████╗  ██║██║ ██╔╝██║████╗  ██║██╔════╝                   ║
║    ██████╔╝███████║██╔██╗ ██║█████╔╝ ██║██╔██╗ ██║██║  ███╗                  ║
║    ██╔══██╗██╔══██║██║╚██╗██║██╔═██╗ ██║██║╚██╗██║██║   ██║                  ║
║    ██████╔╝██║  ██║██║ ╚████║██║  ██╗██║██║ ╚████║╚██████╔╝                  ║
║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                   ║
║                                                                              ║
║                           🏦 ENHANCED SYSTEM 🏦                              ║
║                        💎 Premium Banking Experience 💎                      ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def print_transaction_success(transaction_type, amount, balance):
    """Print success message with nice formatting"""
    print("\n" + "="*60)
    print("🎉 TRANSACTION SUCCESSFUL! 🎉")
    print("="*60)
    print(f"📋 Type: {transaction_type}")
    print(f"💰 Amount: ${amount:.2f}")
    print(f"🏦 New Balance: ${balance:.2f}")
    print("="*60)

def print_account_card(account):
    """Print a beautiful account card"""
    print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                               ACCOUNT CARD                                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  👤 Account Holder: {account.account_owner.full_name:<48} ║
║  🔢 Account Number: {account.account_number:<48} ║
║  💰 Current Balance: ${account.account_balance:<47.2f} ║
║                                                                              ║
║  📅 Banking with us since: Premium Member                                    ║
║  ⭐ Status: Active                                                           ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def print_loading_animation():
    """Print a simple loading animation"""
    import time
    import sys
    
    print("Loading", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="")
        sys.stdout.flush()
    print(" Done! ✅")

def print_goodbye_message():
    """Print a nice goodbye message"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                          Thank You for Banking with Us! 🙏                   ║
║                                                                              ║
║    Your trust is our treasure, your satisfaction our success! 💎            ║
║                                                                              ║
║                         Have a wonderful day! 🌟                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

def print_error_message(error_msg):
    """Print a nicely formatted error message"""
    print("\n" + "⚠️ "*20)
    print(f"❌ ERROR: {error_msg}")
    print("⚠️ "*20 + "\n")

def get_currency_symbol():
    """Get different currency symbols for fun"""
    currencies = ["$", "€", "£", "¥", "₹", "₽"]
    return currencies[0]  # Default to USD

def print_balance_bar(balance, max_balance=5000):
    """Print a visual balance bar"""
    if max_balance == 0:
        max_balance = 1
    
    percentage = min(balance / max_balance, 1.0)
    bar_length = 30
    filled_length = int(bar_length * percentage)
    
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    
    print(f"\n💰 Balance Visualization:")
    print(f"[{bar}] ${balance:.2f}")
    print(f"Progress: {percentage*100:.1f}% of ${max_balance:.2f}")

def print_menu_border():
    """Print decorative menu border"""
    print("🔸" * 25)

if __name__ == "__main__":
    # Test the art functions
    print_welcome_banner()
    print_loading_animation()
