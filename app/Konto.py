class Konto:
    def __init__(self):
        self.saldo = 0

    def przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            self.history += [kwota]

    def przelew_wychodzacy(self, kwota):
        if (self.saldo - kwota) >= 0 and kwota > 0:
            self.saldo -= kwota
            self.history += [-kwota]

    def przelew_ekspresowy(self, kwota):
        if (self.saldo - kwota) >= 0 and kwota > 0:
            self.saldo -= kwota + self.oplata_za_przelew_ekspresowy
            self.history += [-kwota]
            self.history += [-self.oplata_za_przelew_ekspresowy]
