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



zwierz1 = Pies("Azor", 11, "Labrador")
zwierz2 = Zwierze("Kotek Andrzej", 16)

zwierz1.wydajDzwiek()
zwierz2.wydajDzwiek()

zwierz1.podajRase()
#zwierz2.podajRase()