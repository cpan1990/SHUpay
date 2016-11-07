import csv

f = open("credentials.csv", "a+") #creates credentials.csv if it does not exist
f.close()

with open('credentials.csv') as f: #imports contents of credentials.csv as dictionary
    credentials = dict(filter(None, csv.reader(f)))

class Accounts:
    def register(self):
        username = input("Create a username:")
        password = input("Create a password:")

        if username not in credentials:
            credentials[username] = password

            with open("credentials.csv", "a") as csv_file: #writes credentials to credentials.csv and confirms if successful
                writer = csv.writer(csv_file)
                writer.writerow([username,password])
            print("Registration successful")

        else:
            print("Username already exists")

    def authenticate(self):
        username = input("Enter your username:")
        password = input("Enter your password:")

        if username in credentials and credentials[username] == password:
            print("Login successful")
            authenticated = True

        else:
            print("Login failed")
            authenticated = False

accounts = Accounts()