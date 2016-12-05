import unittest
from database_nocsv import Database
from database_nocsv import credentials
from database_nocsv import balancedb

class TestDB(unittest.TestCase):
    def test_registerAccount(self):
        Database.registerAccount(self, "testuser", "testpassword")
        self.assertTrue(credentials["testuser"] == "testpassword")

    def test_updatePassword(self):
        Database.updatePassword(self, "testuser", "testupdatedpassword")
        self.assertTrue(credentials["testuser"] == "testupdatedpassword")

    def test_admin(self):
        self.assertTrue(credentials["admin"] == "open")

    def test_updateBalance(self):
        Database.updateBalance(self, "admin", balance=float(50))
        self.assertTrue(balancedb["admin"] == float(50))

if __name__ == '__main__':
    unittest.main()
