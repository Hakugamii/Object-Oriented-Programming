class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += float(amount)

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= float(amount)
        
    def display_account_info(self):
        print(f"Account Number: {self.__account_number}\nBalance: {self.__balance}")

    def __display_balance(self):
        return print(f"Balance: {self.__balance}")

    def get_account_number(self):
        return self.__account_number
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if float(balance) > 0:
            self.__balance = float(balance)
        else:
            print("Error balance is invalid")
    
maya = BankAccount(90123, 0)

maya.deposit(10)
maya.withdraw(5)
maya.set_balance(-20)
maya.display_account_info()