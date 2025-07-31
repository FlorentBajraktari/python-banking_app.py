# main.py - Optimized Banking System Entry Point
"""
🏦 PROFESSIONAL BANKING SYSTEM
===============================

Complete banking application suite with multiple interfaces:
- Enhanced Console Banking (Full CRUD + Analytics)
- Professional GUI Banking (Tkinter CRUD Interface)
- Analytics Dashboard (Real-time Statistics)
- Creative Launcher (Module Management)

Usage: python main.py

Requirements:
- Python 3.6+
- tkinter (usually included with Python)
- Standard library modules only

Author: Banking Development Team
Version: 1.0 - Optimized
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox, ttk

def check_dependencies():
    """Check if all required modules are available"""
    required_modules = ['json', 'datetime', 'enum', 'collections']
    missing = []
    
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"❌ Missing required modules: {', '.join(missing)}")
        return False
    return True

def check_files():
    """Check if all required files exist"""
    required_files = [
        'Model.py',
        'Enhanced_BankingApp.py', 
        'Professional_Banking_GUI.py',
        'banking_dashboard.py',
        'banking_art.py',
        'Creative_Banking_Launcher.py'
    ]
    
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    
    if missing:
        print(f"❌ Missing required files: {', '.join(missing)}")
        print("Please ensure all banking system files are in the same directory.")
        return False
    return True

def show_main_menu():
    """Show the main application selection menu"""
    print("\n" + "="*80)
    print("🏦 PROFESSIONAL BANKING SYSTEM - MAIN LAUNCHER 🏦")
    print("="*80)
    print("💎 Choose your banking interface:")
    print()
    print("1. 🖥️  Professional GUI Banking (Classic)")
    print("   • Modern Tkinter interface")
    print("   • Full CRUD operations")
    print("   • Real-time statistics")
    print("   • Account management")
    print()
    print("2. ✨ Enhanced Professional GUI (New!)")
    print("   • Ultra-modern card-based interface")
    print("   • Professional color schemes")
    print("   • Enhanced user experience")
    print("   • Real-time dashboard")
    print()
    print("3. 🏦 Enhanced Console Banking")
    print("   • Full-featured console interface")
    print("   • Multi-account management")
    print("   • Transaction history")
    print("   • Data persistence")
    print()
    print("4. 📊 Analytics Dashboard")
    print("   • Real-time banking statistics")
    print("   • Account analysis")
    print("   • Report generation")
    print("   • Data visualization")
    print()
    print("5. 🎨 Creative Launcher (All Modules)")
    print("   • Access all banking modules")
    print("   • Development playground")
    print("   • Module management")
    print("   • Educational demos")
    print()
    print("6. ℹ️  System Information")
    print("7. 🚪 Exit")
    print("="*80)

def launch_professional_gui():
    """Launch the Professional GUI Banking System"""
    print("\n🚀 Launching Professional GUI Banking System...")
    print("📝 Note: Close the GUI window to return to this menu.")
    
    try:
        import tkinter as tk
        from Professional_Banking_GUI import ProfessionalBankingGUI
        
        root = tk.Tk()
        app = ProfessionalBankingGUI(root)
        root.mainloop()
        
        print("✅ GUI session completed.")
        
    except ImportError as e:
        print(f"❌ Error importing GUI components: {e}")
        print("Please ensure tkinter is installed (usually comes with Python)")
    except Exception as e:
        print(f"❌ Error launching GUI: {e}")

def launch_enhanced_professional_gui():
    """Launch the Enhanced Professional GUI Banking System"""
    print("\n🚀 Launching Enhanced Professional GUI Banking System...")
    print("📝 Note: Close the GUI window to return to this menu.")
    
    try:
        import tkinter as tk
        from Enhanced_Professional_GUI import EnhancedProfessionalBankingGUI
        
        root = tk.Tk()
        app = EnhancedProfessionalBankingGUI(root)
        root.mainloop()
        
        print("✅ Enhanced GUI session completed.")
        
    except ImportError as e:
        print(f"❌ Error importing Enhanced GUI components: {e}")
        print("Please ensure tkinter is installed (usually comes with Python)")
    except Exception as e:
        print(f"❌ Error launching Enhanced GUI: {e}")

def launch_enhanced_console():
    """Launch the Enhanced Console Banking System"""
    print("\n🚀 Launching Enhanced Console Banking...")
    
    try:
        from Enhanced_BankingApp import main
        main()
    except Exception as e:
        print(f"❌ Error launching console banking: {e}")

def launch_analytics():
    """Launch the Analytics Dashboard"""
    print("\n🚀 Launching Analytics Dashboard...")
    
    try:
        from banking_dashboard import main
        main()
    except Exception as e:
        print(f"❌ Error launching analytics: {e}")

def launch_creative_system():
    """Launch the Creative Banking Launcher"""
    print("\n🚀 Launching Creative Banking System...")
    
    try:
        from Creative_Banking_Launcher import CreativeBankingLauncher
        launcher = CreativeBankingLauncher()
        launcher.show_main_menu()
    except Exception as e:
        print(f"❌ Error launching creative system: {e}")

def show_system_info():
    """Show system information and file status"""
    print("\n" + "="*60)
    print("📋 SYSTEM INFORMATION")
    print("="*60)
    
    print(f"🐍 Python Version: {sys.version}")
    print(f"📁 Working Directory: {os.getcwd()}")
    
    print("\n📦 MODULE STATUS:")
    modules = [
        ('Model.py', 'Core banking classes and logic'),
        ('Enhanced_BankingApp.py', 'Console banking interface'),
        ('Professional_Banking_GUI.py', 'Classic Tkinter GUI interface'),
        ('Enhanced_Professional_GUI.py', 'Ultra-modern GUI interface'),
        ('banking_dashboard.py', 'Analytics and statistics'),
        ('banking_art.py', 'ASCII art and visual elements'),
        ('Creative_Banking_Launcher.py', 'Creative module launcher')
    ]
    
    for module, description in modules:
        status = "✅ Available" if os.path.exists(module) else "❌ Missing"
        print(f"   {status:<12} {module:<30} - {description}")
    
    print("\n💾 DATA FILES:")
    data_files = ['banking_data.json']
    for file in data_files:
        status = "✅ Exists" if os.path.exists(file) else "📝 Will be created"
        print(f"   {status:<12} {file}")
    
    print("="*60)

def main():
    """Main application entry point"""
    # Check system requirements
    if not check_dependencies():
        print("Please install missing dependencies and try again.")
        return
    
    if not check_files():
        print("Please ensure all files are present and try again.")
        return
    
    print("🎉 Welcome to the Professional Banking System!")
    print("All system checks passed successfully.")
    
    while True:
        show_main_menu()
        
        try:
            choice = input("\n👉 Enter your choice (1-7): ").strip()
            
            if choice == '1':
                launch_professional_gui()
            elif choice == '2':
                launch_enhanced_professional_gui()
            elif choice == '3':
                launch_enhanced_console()
            elif choice == '4':
                launch_analytics()
            elif choice == '5':
                launch_creative_system()
            elif choice == '6':
                show_system_info()
            elif choice == '7':
                print("\n👋 Thank you for using the Professional Banking System!")
                print("Have a great day! 🌟")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1-7.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            print("Please try again or contact support.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
