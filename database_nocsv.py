class Database:
    global credentials
    credentials = {}
    global balancedb
    balancedb = {}
    
    def registerAccount(self, username, password):
        if username not in credentials:
            credentials[username] = password
            print("Registration successful")

        else:
            print("Username already exists")

    def updatePassword(self, username, password):
        credentials.pop(username, None)
        credentials[username] = password

    def updateBalance(self, username, balance):
        balancedb.pop(username, None)
        balancedb[username] = balance

database = Database()
