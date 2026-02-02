class Osoba():
    imie = ""
    nazwisko = ""
    wiek = 0

    def wprowadz(self, imie: str, nazwisko: str, wiek: int) -> None:
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def dane(self):
        # return f"Jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat."
        print(f"Jestem {self.imie} {self.nazwisko}")
        if self.wiek >= 18:
            print("Jesteś pełnoletni")
        else:
            print("Nie jesteś pełnoletni")