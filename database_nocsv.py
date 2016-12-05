global credentials
credentials = {"admin":"open"}
global balancedb
balancedb = {}
global paymentmethoddb
paymentmethoddb = {}
    
class Database:
    def registerAccount(self, username, password):
        if username not in credentials:
            credentials[username] = password
            print("Registration successful")

        else:
            print("Username already exists")

    def updatePassword(self, username, password):
        credentials.pop(username, None)
        credentials[username] = password
        print("Password updated for account " + username)

    def updateBalance(self, username, balance):
        balancedb.pop(username, None)
        balancedb[username] = balance

    def addPaymentMethod(self, username, paymentmethod):
        paymentmethoddb[username] = paymentmethod

database = Database()
