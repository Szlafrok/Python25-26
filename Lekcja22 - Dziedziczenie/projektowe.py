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

class Ptak(Zwierze):
    def __init__(self, imie, wiek, predkoscLotu):
        super().__init__(imie, wiek)
        self.predkoscLotu = predkoscLotu

    def wypiszPredkosc(self):
        print(f"{self.imie} lata z prędkością {self.predkoscLotu} km/h")


class Orzel(Ptak):
    def __init__(self, imie, wiek, predkoscLotu):
        super().__init__(imie, wiek, predkoscLotu)

    def lecisz(self):
        print(f"{self.imie} POTĘŻNY PRZELOT ORŁA z prędkością {self.predkoscLotu}")


# [+++] Proszę napisać klasę Ptak, która dziedziczy po klasie Zwierze.
#       Ptak dodatkowo posiada swoją prędkość lotu wyrażoną w liczbie i potrafi wypisać tę prędkość.

# [++] [Można zrobić, ale potem zrobimy to wspólnie] Proszę napisać klasę Orzel, która
#      dziedziczy po klasie Ptak. Ma takie same parametry, ale dodatkowo ma metodę lecisz(), która
#      wypisuje "POTĘŻNY PRZELOT ORŁA"

# [+] Proszę przetestować napisane klasy.

zwierz1 = Pies("Azor", 11, "Labrador")
zwierz2 = Kot("Andrzej", 16, "Rude")
zwierz3 = Ptak("Leszek", 10, 30)

zwierz3.wypiszPredkosc()
zwierz3.wydajDzwiek()

zwierz1.wydajDzwiek()
zwierz2.wydajDzwiek()

zwierz1.podajRase()

zwierz2.podajUmaszczenie()
zwierz2.miau()

orzel = Orzel("Michał", 200, 1500)
orzel.lecisz()