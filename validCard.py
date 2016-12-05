from database_nocsv import Database
from database_nocsv import credentials
from database_nocsv import paymentmethoddb


#Validates credit card length (no str)
            
def validCard (cardno):
    
    if len(str(cardno)) != 16:
        print ("Please enter 16 digit card number")
        Database.addPaymentMethod (self, username, paymentmethod)
        
    else:
        i = 0
        while i < len(str(cardno)):
            c = (str(cardno))
            if c in range (0,47) or c in range (58,255):
                print ("Invalid value")
                break
            else:
                i = i + 1

    
    
    print ("Successfully added credit card")

paymentmethoddb = validCard
