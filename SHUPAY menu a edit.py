class Menu(object):

    balance = 0
    balance = float(balance)
    money = 0
    money = float(money)

    def deposit(money):
        global balance
        deposit = input("How much: $")
        deposit = float(deposit)
        if deposit <= money:
            balance = balance
            money = money - deposit
            money = float(money)
            deposit = deposit * .1
            deposit = float(deposit)
            balance = deposit + balance
            balance = float(balance)
            print ("You've successfully deposited $",deposit, "into your account.")
            print (bank_balance(balance))
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
        elif ans == "3":
            print ("Thank-You for using SHUPAY!")
            ans=False



