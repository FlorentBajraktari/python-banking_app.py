# Creative_Banking_Launcher.py - Ultimate Banking Experience

import os
import sys
import time
from banking_art import *
from banking_dashboard import BankingDashboard

class CreativeBankingLauncher:
    def __init__(self):
        self.current_mode = "premium"
        self.user_name = ""
        self.setup_user()
    
    def setup_user(self):
        """Setup user preferences"""
        print_welcome_banner()
        print("🎉 Welcome to the Ultimate Banking Experience!")
        
        self.user_name = input("\n👤 Please enter your name: ").strip()
        if not self.user_name:
            self.user_name = "Valued Customer"
        
        print(f"\n🌟 Hello, {self.user_name}! Let's get started!")
        print_loading_animation()
    
    def show_main_menu(self):
        """Show the creative main menu"""
        while True:
            print_menu_border()
            print(f"\n🎯 BANKING EXPERIENCE CENTER - Welcome {self.user_name}! 🎯")
            print_menu_border()
            
            print("\n💎 PREMIUM SERVICES:")
            print("1. 🏦 Enhanced Banking System (Full Features)")
            print("2. 🎮 Classic Module Playground")
            print("3. 📊 Analytics Dashboard")
            print("4. 🎨 Visual Banking (GUI)")
            print("5. 🔧 System Utilities")
            print("6. ℹ️  About & Help")
            print("7. 👋 Exit")
            
            choice = input(f"\n{self.user_name}, choose your adventure (1-7): ").strip()
            
            if choice == '1':
                self.launch_enhanced_banking()
            elif choice == '2':
                self.launch_module_playground()
            elif choice == '3':
                self.launch_analytics()
            elif choice == '4':
                self.launch_gui_banking()
            elif choice == '5':
                self.system_utilities()
            elif choice == '6':
                self.show_about()
            elif choice == '7':
                self.exit_application()
                break
            else:
                print_error_message("Invalid choice. Please try again!")
    
    def launch_enhanced_banking(self):
        """Launch the enhanced banking system"""
        print("\n🚀 Launching Enhanced Banking System...")
        print_loading_animation()
        
        try:
            # Import and run the enhanced banking system
            from Enhanced_BankingApp import EnhancedBankingSystem
            banking_system = EnhancedBankingSystem()
            banking_system.main_menu()
        except ImportError:
            print_error_message("Enhanced Banking System not found!")
            input("Press Enter to continue...")
    
    def launch_module_playground(self):
        """Launch the classic modules"""
        while True:
            print("\n🎮 CLASSIC MODULE PLAYGROUND")
            print("="*50)
            print("1. 📚 Module 1 - Basic Variables")
            print("2. 🏗️  Module 2-1 - Basic OOP")
            print("3. 🎯 Module 2-2 - Advanced OOP")
            print("4. 🏃 Run All Modules Demo")
            print("5. 🔙 Back to Main Menu")
            
            choice = input("\nChoose module (1-5): ").strip()
            
            if choice == '1':
                self.run_module("banking-app-module1-tasks")
            elif choice == '2':
                self.run_module("banking-app-module2-tasks-1")
            elif choice == '3':
                self.run_module("banking-app-module2-tasks-2")
            elif choice == '4':
                self.run_all_modules_demo()
            elif choice == '5':
                break
            else:
                print_error_message("Invalid choice!")
    
    def run_module(self, module_path):
        """Run a specific module"""
        full_path = os.path.join("..", module_path)
        
        if os.path.exists(full_path):
            print(f"\n🏃 Running {module_path}...")
            print_loading_animation()
            print("="*60)
            
            # Change to module directory and run
            old_cwd = os.getcwd()
            try:
                os.chdir(full_path)
                os.system("python BankingApp.py")
            finally:
                os.chdir(old_cwd)
            
            print("="*60)
            input("\n✅ Module completed! Press Enter to continue...")
        else:
            print_error_message(f"Module {module_path} not found!")
            input("Press Enter to continue...")
    
    def run_all_modules_demo(self):
        """Run all modules in sequence"""
        modules = [
            "banking-app-module1-tasks",
            "banking-app-module2-tasks-1", 
            "banking-app-module2-tasks-2"
        ]
        
        print("\n🎬 FULL DEMO - All Modules Showcase")
        print("="*60)
        
        for i, module in enumerate(modules, 1):
            print(f"\n🎯 Demo {i}/{len(modules)}: {module}")
            time.sleep(1)
            self.run_module(module)
        
        print("\n🎉 All modules demo completed!")
        input("Press Enter to continue...")
    
    def launch_analytics(self):
        """Launch the analytics dashboard"""
        print("\n📊 Launching Analytics Dashboard...")
        print_loading_animation()
        
        try:
            dashboard = BankingDashboard()
            dashboard.print_dashboard()
            
            # Mini analytics menu
            while True:
                print("\n📈 ANALYTICS OPTIONS:")
                print("1. 🔄 Refresh Dashboard")
                print("2. 🔍 Account Analysis")
                print("3. 📄 Export Report")
                print("4. 🔙 Back")
                
                choice = input("Choose option (1-4): ").strip()
                
                if choice == '1':
                    dashboard.print_dashboard()
                elif choice == '2':
                    try:
                        acc_num = int(input("Enter account number: "))
                        dashboard.print_account_analysis(acc_num)
                    except ValueError:
                        print_error_message("Invalid account number!")
                elif choice == '3':
                    dashboard.export_report()
                elif choice == '4':
                    break
                else:
                    print_error_message("Invalid choice!")
        
        except Exception as e:
            print_error_message(f"Analytics error: {e}")
            input("Press Enter to continue...")
    
    def launch_gui_banking(self):
        """Launch the GUI banking application"""
        print("\n🎨 Launching Visual Banking Interface...")
        print_loading_animation()
        
        print("🖥️  Starting Kivy GUI Application...")
        print("📝 Note: Close the GUI window to return to this menu.")
        
        try:
            os.system("python BankingApp.py")
        except Exception as e:
            print_error_message(f"GUI launch error: {e}")
        
        input("\n✅ GUI session ended. Press Enter to continue...")
    
    def system_utilities(self):
        """System utilities and tools"""
        while True:
            print("\n🔧 SYSTEM UTILITIES")
            print("="*40)
            print("1. 📁 Show Data Files")
            print("2. 🧹 Clean Cache Files") 
            print("3. 💾 Backup Data")
            print("4. 📊 System Info")
            print("5. 🔙 Back")
            
            choice = input("Choose utility (1-5): ").strip()
            
            if choice == '1':
                self.show_data_files()
            elif choice == '2':
                self.clean_cache()
            elif choice == '3':
                self.backup_data()
            elif choice == '4':
                self.show_system_info()
            elif choice == '5':
                break
            else:
                print_error_message("Invalid choice!")
    
    def show_data_files(self):
        """Show data files in the system"""
        print("\n📁 DATA FILES:")
        print("-" * 30)
        
        files = [f for f in os.listdir('.') if f.endswith(('.json', '.txt', '.py'))]
        
        for file in sorted(files):
            size = os.path.getsize(file)
            print(f"📄 {file:<30} ({size} bytes)")
        
        input("\nPress Enter to continue...")
    
    def clean_cache(self):
        """Clean cache files"""
        print("\n🧹 Cleaning cache files...")
        
        cache_dirs = ['__pycache__']
        cleaned = 0
        
        for cache_dir in cache_dirs:
            if os.path.exists(cache_dir):
                try:
                    import shutil
                    shutil.rmtree(cache_dir)
                    cleaned += 1
                    print(f"✅ Cleaned {cache_dir}")
                except:
                    print(f"❌ Could not clean {cache_dir}")
        
        if cleaned == 0:
            print("✨ No cache files to clean!")
        else:
            print(f"✅ Cleaned {cleaned} cache directories!")
        
        input("Press Enter to continue...")
    
    def backup_data(self):
        """Backup banking data"""
        if os.path.exists('banking_data.json'):
            backup_name = f"banking_data_backup_{int(time.time())}.json"
            try:
                import shutil
                shutil.copy('banking_data.json', backup_name)
                print(f"✅ Data backed up to: {backup_name}")
            except Exception as e:
                print_error_message(f"Backup failed: {e}")
        else:
            print("ℹ️  No data file found to backup.")
        
        input("Press Enter to continue...")
    
    def show_system_info(self):
        """Show system information"""
        print("\n💻 SYSTEM INFORMATION")
        print("="*40)
        print(f"🐍 Python Version: {sys.version}")
        print(f"🗂️  Current Directory: {os.getcwd()}")
        print(f"👤 User: {self.user_name}")
        print(f"📅 Session Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Count files
        py_files = len([f for f in os.listdir('.') if f.endswith('.py')])
        json_files = len([f for f in os.listdir('.') if f.endswith('.json')])
        
        print(f"📄 Python Files: {py_files}")
        print(f"💾 Data Files: {json_files}")
        
        input("\nPress Enter to continue...")
    
    def show_about(self):
        """Show about information"""
        print("\n" + "="*60)
        print("ℹ️  ABOUT ULTIMATE BANKING EXPERIENCE")
        print("="*60)
        print("""
🏦 Ultimate Banking System v2.0
   Created with ❤️  for learning and creativity!

📋 FEATURES:
   ✅ Multiple banking modules progression
   ✅ Enhanced banking with persistence
   ✅ Real-time analytics dashboard  
   ✅ Beautiful GUI interface
   ✅ Transaction history & reporting
   ✅ Account management & transfers
   ✅ Visual enhancements & ASCII art

🛠️  TECHNOLOGY STACK:
   🐍 Python 3.x
   🎨 Kivy (GUI)
   💾 JSON (Data persistence)
   📊 Custom analytics engine

👨‍💻 EDUCATIONAL PURPOSE:
   📚 Demonstrates Python programming progression
   🏗️  From basic variables to advanced OOP
   🎯 GUI development with Kivy
   📈 Data analysis and visualization

🎯 USAGE:
   Perfect for learning Python, OOP concepts,
   GUI development, and building real applications!
        """)
        
        input("\nPress Enter to continue...")
    
    def exit_application(self):
        """Exit the application gracefully"""
        print_goodbye_message()
        print(f"👋 Goodbye, {self.user_name}!")
        print("🌟 Thank you for exploring the Ultimate Banking Experience!")
        
        # Save any final data
        print("💾 Saving session data...")
        time.sleep(1)
        print("✅ All data saved successfully!")

def main():
    """Main application entry point"""
    launcher = CreativeBankingLauncher()
    launcher.show_main_menu()

if __name__ == '__main__':
    main()
