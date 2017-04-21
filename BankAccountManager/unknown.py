import os

"""Create a class called Account which will be an abstract class 
for three other classes called CheckingAccount, SavingsAccount and BusinessAccount. 
Manage credits and debits from these accounts through an ATM style program."""

"""Create a database for ATM"""
"""Create a program which takes data from spreadsheet and puts it into the database by itself"""


class Account(object):

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def name_balance(self):
        
        print 'Name: %s' % self.name
        print 'Balance: %s' % self.balance
        print '*'*60

    def check_balance

client1 = Account('Sabih', 60000)
client2 = Account('Geos', 50000000)

client1.name_balance()
client2.name_balance()

class CurrentAccount(Account):

    def __init__(self, name, balance, withdrawAmount):
        self.name = name
        self.balance = balance
        self.withdrawAmount = withdrawAmount

    def name_balance(self):

        print 'Name: %s' % self.name
        print 'Balance: %s' % self.balance
        print 'withdrawAmount: %s' % self.withdrawAmount
        print '*'*60



client1 = CurrentAccount('Unimroy', 70000000, 99999999999)
client1.name_balance()











