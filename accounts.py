import csv
from database import Database

f = open("credentials.csv", "a+")  # creates credentials.csv if it does not exist
f.close()

with open('credentials.csv') as f:  # imports contents of credentials.csv as dictionary
    credentials = dict(filter(None, csv.reader(f)))

class Accounts:
    def register(self):
        username = input("Create a username:")
        password = input("Create a password:")
        password2 = input("Confirm your password:")

        if (any(x.isupper() for x in password) and any(x.islower() for x in password)
            and any(x.isdigit() for x in password) and len(password) >= 8):

            if password == password2:
                Database.registerAccount(self, username, password)

            else:
                print("Passwords do not match. Please try again.")
                self.register()

        else:
            print("Please enter a password with at least 8 characters and at least 1 upper, 1 lower and 1 number.")
            self.register()

    def authenticate(self):
        username = input("Enter your username:")
        password = input("Enter your password:")

        if username in credentials and credentials[username] == password:
            print("Login successful")
            return username

        else:
            print("Login failed")
            self.authenticate()

    def updatePassword(self):
        username = self.authenticate()
        password = input("Enter your new password:")
        password2 = input("Confirm your new password:")

        if password2 == password:
            Database.updatePassword(self, username, password)

accounts = Accounts()
