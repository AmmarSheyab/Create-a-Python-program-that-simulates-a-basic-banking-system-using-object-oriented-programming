#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Account:
    def __init__(self, holder_name, balance=0):
        self.holder_name = holder_name
        self.account_number = random.randint(10000, 99999)  # Generate a random 5-digit account number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display_info(self):
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")


# In[3]:


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, holder_name, initial_balance=0):
        if initial_balance < 0:
            print("Invalid initial balance. Please provide a non-negative amount.")
            return None

        new_account = Account(holder_name, initial_balance)
        self.accounts.append(new_account)
        print(f"Account created successfully for {holder_name} with account number: {new_account.account_number}")
        return new_account

    def get_account_by_number(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        print("Account not found.")
        return None

    def find_highest_balance_account(self):
        if not self.accounts:
            print("No accounts found.")
            return None
        max_balance_account = max(self.accounts, key=lambda account: account.balance)
        return max_balance_account


# In[4]:


bank = Bank()

# Creating accounts
account1 = bank.create_account("Alice", 1000)
account2 = bank.create_account("Bob", 500)
account3 = bank.create_account("Eve", 1500)


# In[5]:


# Performing transactions
account1.deposit(500)
account2.withdraw(200)
account3.deposit(1000)
account3.withdraw(2000)


# In[6]:


# Displaying account details
print("\nAccount Details:")
account1.display_info()
account2.display_info()
account3.display_info()


# In[7]:


# Finding account with the highest balance
highest_balance_account = bank.find_highest_balance_account()
if highest_balance_account:
    print("\nAccount with the highest balance:")
    highest_balance_account.display_info()


# In[ ]:





# In[ ]:





# In[ ]:




