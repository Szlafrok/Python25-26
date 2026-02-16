class Zwierze():

    def __init__(self, imie: str, wiek: int):
        print("Utworzono zwierzaka!")
        self.imie = imie
        self.wiek = wiek

    def wydajDzwiek(self): # IMIĘZWIERZAKA wydaje dźwięk
        print(f"{self.imie} wydaje dźwięk.")

    def jedz(self):
        print(f"{self.imie} je sobie jedzonko.")


class Pies(Zwierze):
    def __init__(self, imie, wiek, rasa):
        super().__init__(imie, wiek)
        self.rasa = rasa

    def podajRase(self):
        print(f"{self.imie} jest rasy {self.rasa}")

class Kot(Zwierze):
    def __init__(self, imie, wiek, umaszczenie):
        super().__init__(imie, wiek)
        self.umaszczenie = umaszczenie

    def podajUmaszczenie(self):
        print(f"{self.imie} ma umaszczenie {self.umaszczenie}")

    def miau(self):
        print("≽^•⩊•^≼")


# Klasa kot dziedzicząca po Zwierzę
# Kot posiada dodatkowo swoje umaszczenie (barwę sierści)
# Potrafi wypisać to umaszczenie

zwierz1 = Pies("Azor", 11, "Labrador")
zwierz2 = Kot("Andrzej", 16, "Rude")

zwierz1.wydajDzwiek()
zwierz2.wydajDzwiek()

zwierz1.podajRase()

zwierz2.podajUmaszczenie()
zwierz2.miau()