import random

class AccountManager:
    def __init__(self):
        self.accounts = {}  # Initialize a dictionary to hold all accounts

# creating a account
    def create_acc(self):
        name = input("Enter your name: ")
        mobile_no = input("Enter your mobile no.: ")  # Store as string to preserve leading zeros
        ac_id = random.randint(10000, 100000)
        print(f"Your personal account ID is: {ac_id}")
        password = input("Enter your password (4 digits): ")
        if len(password) == 4 and password.isdigit():
            self.accounts[ac_id] = {
                'name': name,
                'mobile_no': mobile_no,
                'password': password,
                'details': {
                    'current_amount': 0,  # Initialize current amount
                    'transactions': []  # Initialize transaction history
                }
            }
            print("Account created successfully.")
        else:
            print("Password must be 4 digits.")

#pvt function to set inital amt to 0
    def __current_amount(self, ac_id):
        # Initialize or update current amount for the account
        self.accounts[ac_id]['details']['current_amount'] = 0  # Set initial amount to 0 or desired value

#function to verify details
    def verify_account(self, ac_id):
        if ac_id in self.accounts:
            password = input("Enter your password: ")
            if self.accounts[ac_id]['password'] == password:
                return True
            else:
                print("Incorrect password.")
                return False
        else:
            print("Account ID not found.")
            return False


#to display the account details
    def view_details(self, ac_id):
        if self.verify_account(ac_id):
            print(self.accounts[ac_id])


#to display the current amount in account
    def current_amt(self, ac_id):
        if self.verify_account(ac_id):
            print("Your current amount is: ", self.accounts[ac_id]['details']['current_amount'])


#to deposit money to self account
    def deposit(self, ac_id):
        if self.verify_account(ac_id):
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 0:
                self.accounts[ac_id]['details']['current_amount'] += amount
                print("Amount deposited successfully")
                self.current_amt(ac_id)
            else:
                print("Deposit amount must be positive.")


#to withdraw the money from self account
    def withdraw(self, ac_id):
        if self.verify_account(ac_id):
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > 0 and amount <= self.accounts[ac_id]['details']['current_amount']:
                self.accounts[ac_id]['details']['current_amount'] -= amount
                print("Amount withdrawn successfully")
                self.current_amt(ac_id)
            else:
                print("Invalid withdrawal amount.")



    def check(self, ac_id):
        if self.verify_account(ac_id):
            name = input("Enter your name: ")
            mobile_no = input("Enter your mobile no.: ")
            account = self.accounts[ac_id]
            if (account['name'] == name and 
                account['mobile_no'] == mobile_no):
                print("Information verified successfully")
                print(self.accounts[ac_id])
            else:
                print("Invalid information. Please try again.")


#to update account details
    def update(self, ac_id):
        if self.verify_account(ac_id):
            name = input("Enter your current name: ")
            mobile_no = input("Enter your current mobile no.: ")
            account = self.accounts[ac_id]
            if (account['name'] == name and 
                account['mobile_no'] == mobile_no):
                print("Information verified successfully")
                print("Enter your choice which you want to update\n1. Name\n2. Mobile no.\n3. Password \n4. Exit")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    new_name = input("Enter your new name: ")
                    account['name'] = new_name
                    print("Name updated successfully")
                elif choice == 2:
                    new_mobile = input("Enter your new mobile no.: ")
                    account['mobile_no'] = new_mobile
                    print("Mobile no. updated successfully")
                elif choice == 3:
                    while True:
                        new_password = input("Enter your new password: ")
                        if len(new_password) == 4 and new_password.isdigit():
                            account['password'] = new_password
                            print("Password updated successfully")
                            break
                        else:
                            print("Invalid format of password. Please try again.")
                elif choice == 4:
                    return
                else:
                    print("Invalid choice.")
            else:
                print("Invalid information. Please try again.")



#to delete account
    def delete(self, ac_id):
        if self.verify_account(ac_id):
            name = input("Enter your name: ")
            mobile_no = input("Enter your mobile no.: ")
            account = self.accounts[ac_id]
            if (account['name'] == name and 
                account['mobile_no'] == mobile_no):
                del self.accounts[ac_id]
                print("Account deleted successfully.")
            else:
                print("Invalid information. Please try again.")


#to transfer money to another account
    def send_money(self, ac_id):
       if self.verify_account(ac_id):
           recipient_ac_id = int(input("Enter the account ID of the payee: "))
           if recipient_ac_id in self.accounts:
               amount = int(input("Enter the amount you want to transfer: "))
               if amount > 0 and self.accounts[ac_id]['details']['current_amount'] >= amount:
                   self.accounts[ac_id]['details']['current_amount'] -= amount
                   self.accounts[recipient_ac_id]['details']['current_amount'] += amount
                   print("Amount transferred successfully.")
               else:
                   print("Invalid transfer amount.")
           else:
               print("Payee account ID not found.")




class Starting:
    def __init__(self):
        self.bank = AccountManager() 
        self.main_menu()

    def main_menu(self):
        while True:
            print("==== Welcome to the Banking System ====")
            print("Choose your option\n1. Create Account\n2. Use Account\n3. Update Account\n4. Delete Account\n5.Transfer money\n6.Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.bank.create_acc()
            elif choice == 2:
                ac_id = int(input("Enter your account ID: "))
                print("Choose your option\n1. Deposit\n2. Withdraw\n3. Check\n4. View Details\n5. Exit")
                choice2 = int(input("Enter your choice: "))
                if choice2 == 1:
                    self.bank.deposit(ac_id)
                elif choice2 == 2:
                    self.bank.withdraw(ac_id)
                elif choice2 == 3:
                    self.bank.check(ac_id)
                elif choice2 == 4:
                    self.bank.view_details(ac_id)
                elif choice2 == 5:
                    continue
                else:
                    print("Invalid choice.")
            elif choice == 3:
                ac_id = int(input("Enter your account ID: "))
                self.bank.update(ac_id)
            elif choice == 4:
                ac_id = int(input("Enter your account ID: "))
                self.bank.delete(ac_id)
            elif choice == 5:
                ac_id = int(input("Enter your account ID: "))
                self.bank.send_money(ac_id)
            elif choice == 6:
                print("Thank you for using the Banking System.")
                break
            else:
                print("Invalid choice.")

# Start the application
Starting()