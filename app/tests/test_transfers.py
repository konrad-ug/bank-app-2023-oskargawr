import unittest

from ..KontoOsobiste import KontoOsobiste


class TestTransfer(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "96001010101"
    }

    def test_incoming_transfer(self):
        first_account = KontoOsobiste(self.personal_data["name"], self.personal_data[
            "surname"], self.personal_data["pesel"])
        first_account.przelew_przychodzacy(100)
        self.assertEqual(first_account.saldo, 100, "Saldo nie jest równe 100!")

    def test_outgoing_transfer(self):
        first_account = KontoOsobiste(self.personal_data["name"], self.personal_data[
            "surname"], self.personal_data["pesel"])
        first_account.saldo = 120
        first_account.przelew_wychodzacy(100)
        self.assertEqual(first_account.saldo, 20,
                         "Saldo nie jest poprawne!")

    def test_outgoing_transfer_with_insufficient_funds(self):
        first_account = KontoOsobiste(self.personal_data["name"], self.personal_data[
            "surname"], self.personal_data["pesel"])
        first_account.saldo = 120
        first_account.przelew_wychodzacy(200)
        self.assertEqual(first_account.saldo, 120,
                         "Saldo nie jest poprawne!")

    def test_incoming_transfer_with_incorrrect_ammount(self):
        first_account = KontoOsobiste(self.personal_data["name"], self.personal_data[
            "surname"], self.personal_data["pesel"])
        first_account.saldo = 120
        first_account.przelew_przychodzacy(-20)
        self.assertEqual(first_account.saldo, 120, "Saldo nie jest poprawne!")

    def test_outgoing_transfer_with_promo_code(self):
        first_account = KontoOsobiste(
            self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"], "PROM_123")
        first_account.przelew_wychodzacy(20)
        self.assertEqual(first_account.saldo, 50 - 20,
                         "Saldo nie jest poprawne!")
