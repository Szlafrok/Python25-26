class Student():
    nazwisko = ""
    ocena_matma = 0.0
    ocena_wf = 0.0
    ocena_informatyka = 0.0
    czyzaliczone = True

    def __init__(self, nazwisko: str , ocena_matma: float,ocena_wf: float,ocena_informatyka: float,) -> None:
        #przypisujemy wprowadzone dane
        self.nazwisko = nazwisko

        if ocena_matma <= 6 and ocena_wf <= 6 and ocena_informatyka <= 6:
            self.ocena_matma = ocena_matma
            self.ocena_wf = ocena_wf
            self.ocena_informatyka = ocena_informatyka
        else:
            raise ValueError
        
        # liczymy średnią
        srednia = (self.ocena_matma + self.ocena_wf + self.ocena_informatyka) / 3

        #sprawdzamy czy zaliczylismy
        if srednia >= 3:
            self.czyzaliczone = True
        else:
            self.czyzaliczone = False

    def wypisz_oceny(self):
        print(f"Ocena z matmy: {self.ocena_matma}")
        print(f"Ocena z wf: {self.ocena_wf}")
        print(f"Ocena z informatyki: {self.ocena_informatyka}")
        # Wypisujemy oceny

    def zdane(self):
        #wypisyujemy zaliczenie z wszystkiego
        if self.czyzaliczone:
            print("Zdałeś!")
        else:
            print("Nie zdałeś")



# class Student:
#     # Słownik przechowujący maksymalną liczbę ocen dla każdej klasy
#     MAKS_OCENY = {
#         1: 5,
#         2: 5,
#         3: 5,
#         4: 10,
#         5: 11,
#         6: 13,
#         7: 14,
#         8: 16
#     }

#     def __init__(self, klasa: int, nazwisko: str, *oceny: float) -> None:
#         # Sprawdzenie, czy podana klasa jest poprawna
#         if klasa not in self.MAKS_OCENY:
#             raise ValueError("Niepoprawna klasa")

#         # Pobranie maksymalnej liczby ocen dla danej klasy
#         max_oceny = self.MAKS_OCENY[klasa]

#         # Sprawdzenie, czy liczba podanych ocen mieści się w dozwolonym zakresie
#         if not (1 <= len(oceny) <= max_oceny):
#             raise ValueError(f"Niepoprawna liczba ocen dla klasy {klasa}")

#         # Sprawdzenie, czy wszystkie oceny są w zakresie 0-6
#         for ocena in oceny:
#             if not (0 <= ocena <= 6):
#                 raise ValueError("Ocena poza zakresem 0-6")

#         # Przypisanie nazwiska
#         self.nazwisko = nazwisko

#         # Zapisanie ocen w liście
#         self.oceny = list(oceny)

#         # Obliczenie średniej i określenie, czy student zdał
#         # Średnia >= 3 oznacza zaliczenie
#         self.czyzaliczone = sum(self.oceny) / len(self.oceny) >= 3

#     # Metoda wypisująca wszystkie oceny studenta
#     def wypisz_oceny(self):
#         for i, ocena in enumerate(self.oceny, 1):
#             print(f"Ocena {i}: {ocena}")

#     # Metoda informująca, czy student zdał
#     def zdane(self):
#         print("Zdałeś!" if self.czyzaliczone else "Nie zdałeś")

damian = Student("Krupa", 3, 4, 7)
damian.zdane()
damian.wypisz_oceny()

############################
"""
Biorę pod uwagę pierwszą klasę, w drugiej podziały się dziwne rzeczy, plus wygląda trochę na wygenerowaną czatem, mam rację?

a) Bardzo ładnie, ale sprawdziłeś tylko, czy średnia ocen jest >= 3.0, a na zaliczenie każda ocena musi być >= 3.0
   Poza tym ekstra! 
   2.5 / 3.0

b) OK -> 2.0 / 2.0

c) było OK pod drugą klasę, więc raczej OK -> 1.0 / 1.0

d) OK, można jeszcze dopisać że metody od średniej i zaliczeń zwracają None, ale przy konstruktorze jest
   więc dla mnie to wystarczy -> 2.0 / 2.0

e) Zgłoszenie wyjątku OK, warto dopisać w nawiasie opis błędu, np. ValueError("Niepoprawna ocena!").
   Mam natomiast uwagę do warunków - sprawdzasz tylko, czy ocena jest <= 6, co nie potwierdza 
   wszystkich kryteriów wymienionych w zadaniu -> 2.0 / 3.0


Wkradły się miejscami dziwne rzeczy i błędy nieuwagi, ale zadania rozwiązane całkiem ładnie. Brawo ;)
SUMA: 9.5 / 11.0 ⭐➕➕


"""