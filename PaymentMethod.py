#MAIN MODULE
    
import database_nocsv
from database_nocsv import Database
from database_nocsv import credentials
from database_nocsv import paymentmethoddb
from accounts import Accounts
import blank_mod
import validDOB
import quantity
import validCard

print ("Enter your information to add a credit card")

f_name = input ("What is your first name: ")
blank_mod.blank_mod(f_name)
l_name = input ("What is your last name: ")
blank_mod.blank_mod (l_name)
date = input ("Please enter your date of birth, mm-dd-yyyy: ")

verify_age = validDOB.age (date)
if verify_age != 0:
    print ("User is %s years of age " %(verify_age))
    
qty_ord = eval(input ("Enter CVV#: "))
if blank_mod.blank_mod(qty_ord) == 1:
    quantity.quantity(qty_ord)

credit = eval(input ("Enter credit card number: "))
if blank_mod.blank_mod(credit) == 1:
    validCard.validCard(credit)
    Database.addPaymentMethod (validCard, qty_ord, paymentmethoddb)
    

