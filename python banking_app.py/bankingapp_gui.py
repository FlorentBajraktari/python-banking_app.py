from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.properties import StringProperty, ObjectProperty

# Assuming BankAccountOwner and BankAccount classes are defined somewhere

class BankAccountOwner:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name

class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = initial_balance

    def get_account_balance(self):
        return self.balance

    def set_account_balance(self, new_balance):
        self.balance = new_balance

class PopupMessage(Popup):
    message_text = StringProperty()

    def dismiss(self):
        super().dismiss()

class BankingAppGUI(BoxLayout):
    owner_label_text = StringProperty()
    balance_label_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create account owner and bank account
        self.account_owner = BankAccountOwner("Filan", "Fisteku")
        self.bank_account = BankAccount(123456, self.account_owner, 500.0)

        # Set initial values for labels
        self.update_labels()

    def update_labels(self):
        self.owner_label_text = f"Account Owner: {self.account_owner.get_first_name()} {self.account_owner.get_last_name()}"
        self.balance_label_text = f"Balance: {self.bank_account.get_account_balance()}"

    def perform_action(self):
        action = self.ids.action_spinner.text
        amount_str = self.ids.amount_input.text.strip()

        if not amount_str:
            self.show_popup("Invalid amount input.")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            self.show_popup("Invalid amount input.")
            return

        if action == 'Deposit':
            if amount >= 0:
                self.bank_account.set_account_balance(self.bank_account.get_account_balance() + amount)
                self.update_labels()
            else:
                self.show_popup("Invalid amount input.")
        elif action == 'Withdraw':
            if 0 < amount <= self.bank_account.get_account_balance():
                self.bank_account.set_account_balance(self.bank_account.get_account_balance() - amount)
                self.update_labels()
            else:
                self.show_popup("Insufficient balance.")
        else:
            self.show_popup("Invalid action selected.")

    def show_popup(self, message):
        popup = PopupMessage(message_text=message)
        popup.open()

class BankingApp(App):
    def build(self):
        return BankingAppGUI()

if __name__ == '__main__':
    BankingApp().run()
