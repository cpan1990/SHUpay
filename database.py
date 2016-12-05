import csv

class Database:
    def __init__(self, username, password, authenticated_user):
        self.username = username
        self.password = password
        self.authenticated_user = authenticated_user

    def registerAccount(self, username, password):
        f = open("credentials.csv", "a+")  # creates credentials.csv if it does not exist
        f.close()

        with open('credentials.csv') as f:  # imports contents of credentials.csv as dictionary
            credentials = dict(filter(None, csv.reader(f)))

        if username not in credentials:
            credentials[username] = password

            with open("credentials.csv", "a") as csv_file: #writes credentials to credentials.csv and confirms if successful
                writer = csv.writer(csv_file)
                writer.writerow([username,password])
            print("Registration successful")

        else:
            print("Username already exists")

    def updatePassword(self, username, password):
        f = open("credentials.csv", "a+")  # creates credentials.csv if it does not exist
        f.close()

        with open('credentials.csv') as f:  # imports contents of credentials.csv as dictionary
            credentials = dict(filter(None, csv.reader(f)))

        credentials[username] = password

        with open("credentials.csv",
                  "a") as csv_file:  # writes credentials to credentials.csv and confirms if successful
            writer = csv.writer(csv_file)
            writer.writerow([username, password])
        print("Password changed successfully.")