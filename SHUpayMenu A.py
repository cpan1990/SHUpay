from database_nocsv import Database
from database_nocsv import balancedb
from accounts import Accounts
from database_nocsv import credentials
     
class Menu(object):

    balance = 0.0
    balance = float(balance)
    money = 0.0
    money = float(money)

    def deposit(money):
        global balance
        deposit = input("How much: $")
        deposit = float(deposit)
        if deposit <= money:
            deposit = float(deposit)
            balance = balance + deposit
            balance = float(balance)
        print ("You've successfully deposited $",deposit, "into your account.")
        Database.updateBalance(username, balance)
        return balance

    def bank_balance(balance):
        print ("Balance: $", balance) 
        return balance

    ans = True
    while ans:

        print ("""
       Welcome to SHUPAY
     
       Your Transaction Options Are:
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       1) Deposit Money
       2) Check Balance
       3) Quit SHUPAY""")
    
        ans= input ("Choose your option: ")
    
        if ans ==  "1":
            deposit = deposit (money)
        elif ans == "2":
            balance = bank_balance(balance)
            Database.updateBalance (deposit, bank_balance, balance)
        elif ans == "3":
            print ("Thank-You for using SHUPAY!")
            ans=False


