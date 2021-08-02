'''
Author: Trang Ha Nguyen (Helen)
Date: Aug 2, 2021

Title: Banking App using OOP

Parent class: User (store and display user info)
Child class: Bank (store info on account balance, amount; allow for deposit, withdraw, and view balance)
'''

# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print('Personal Information\n')
        print('Name:', self.name)
        print('Age:', self.age)
        print('Gender:', self.gender)

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('Updated account balance is:', self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if (self.amount > self.balance):
            print('Insufficient funds. Account balance is', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('Successful withdrawal. Updated account balance is:', self.balance)

    def view_balance(self):
        self.show_info()
        print('Account balance:', self.balance)