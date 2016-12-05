from database_nocsv import Database
from database_nocsv import credentials

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
        global username
        username = input("Enter your username:")
        password = input("Enter your password:")

        if username in credentials and credentials[username] == password:
            print("Login successful")
            global authenticated
            authenticated = True
            return username

        else:
            print("Login failed, please try again.")
            global authenticated
            authenticated = False
            self.authenticate()

    def update_password(self):
        self.authenticate()
        if authenticated == True:
            password = input("Create a new password:")
            password2 = input("Confirm your new password:")

        if (any(x.isupper() for x in password) and any(x.islower() for x in password)
            and any(x.isdigit() for x in password) and len(password) >= 8):

            if password == password2:
                Database.registerAccount(self, username, password)

            else:
                print("Passwords do not match. Please try again.")
                self.update_password()

        else:
            print("Please enter a password with at least 8 characters and at least 1 upper, 1 lower and 1 number.")
            self.update_password()
            
    def check_forget_pass(self):
        print ('Did you forget the Password press 1 for Y and 2 for No')
        option = input("Create a password:")
        if option == 2:
            self.authenticate()
        else:
            self.validate_secret_question()

    def validate_secret_question(self):
        print ('Answer the Secret Qustion)#n')
        print ('which college did you attend ')
        college_name = input()
        if college_name.upper()=='SACRED HEART UNIVERSITY':
            self.update_password()
        else:
            print('entered value mismatching')

accounts = Accounts()
