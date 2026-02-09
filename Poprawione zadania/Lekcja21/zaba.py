class Student():
    def __init__(self,nazwisko: str,ocena_matematyka: float, ocena_informatyka: float,ocena_wf: float):
        self.nazwisko = nazwisko#wprowadza nazwisko i oceny do klasy
        self.ocena_matematyka = ocena_matematyka
        self.ocena_informatyka = ocena_informatyka
        self.ocena_wf = ocena_wf

        self.srednia = (ocena_informatyka + ocena_matematyka + ocena_wf) / 3 #wprowadza do klasy srednia ocen // nie do klasy tylko do obiektu ;)
        self.czy_zaliczyl = ocena_informatyka >= 3.0 and ocena_matematyka >= 3.0 and ocena_wf >= 3.0 #wprowadza do klas info czy osoba ma wszystkie oceny większe lub równe 3(czy zdała)

    def wypisz_oceny(self):#wypisuje oceny
        print(f"Matematyka: {self.ocena_matematyka}")
        print(f"Informatyka: {self.ocena_informatyka}")
        print(f"WF: {self.ocena_wf}")

    def zdane(self):#wypisuje na podstawie "czy_zaliczyl" czy osoba zdala
        if self.czy_zaliczyl:
            print("Zdałeś!")
        else:
            print("Nie zdałeś ):")


Jan = Student(nazwisko = "Nowak",ocena_matematyka = 2.3,ocena_informatyka = 4.1,ocena_wf = 3.6)

Jan.wypisz_oceny()
Jan.zdane()

"""
Uwagi:

a)  Super, bez zastrzeżeń ;) 3.0 / 3.0

b)  Bardzo ładnie :D 2.0 / 2.0

c)  Spoko, natomiast czepię się, że obiekt Jan powinien być nazwany z małej litery. 
    Proszę na to uważać, natomiast jest to drobna rzecz i obiekt jest zrobiony poprawnie ;)
    -> 1.0 / 1.0

d)  Spoko, tylko bym dodał przy metodach że zwracają None + uwaga do komentarzy przy linijkach 8 i 9 ;)
    -> 1.5 / 2.0

e)  Brak rozw.

Sumarycznie: 7.5 / 11.0 -> ⭐➕

Bardzo ładne rozwiązania :D 
Jedyne co to ta uwaga do komentarzy ;P

"""