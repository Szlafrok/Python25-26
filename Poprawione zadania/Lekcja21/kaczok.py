class Student():
    nazwisko = ""
    ocena_wf = 0.0
    ocena_matma = 0.0
    ocena_informatyka = 0.0
    srednia = 0.0
    zdanie = None

    
    
    
    
    
    def __init__(self, nazw: str, wf: float, inf: float, matma: float) -> None:
        self.nazwisko = nazw
        self.ocena_wf = wf
        self.ocena_informatyka = inf
        self.ocena_matma = matma

        # Przeniosłem tutaj i dodałem self. do zmiennych
        if self.ocena_informatyka or self.ocena_matma or self.ocena_wf != 2.0 or 3.0 or 3.5 or 4.0 or 4.5 or 5.0:
            raise NameError("Error 400")


    def zdane(self) -> None:
        if self.ocena_wf > 3.0:
            if self.ocena_informatyka > 3.0:
                if self.ocena_matma > 3.0:
                    zdane = True
                else:
                    zdane = False
            else:
                zdane = False
        else:
            zdane = False
        print(zdane)

    def oblicz_srednia(self) -> float:
        self.srednia = (self.ocena_wf + self.ocena_informatyka + self.ocena_matma) / 3
        return self.srednia


Szczepan = Student("ziemniaczany",2.0,3.5,4.5) # była literówka w skrypcie
print(Szczepan.oblicz_srednia())
Szczepan.zdane()

"""
a)  Spoko, tylko według zadania miałeś określać średnią i zaliczenie w konstruktorze ;P
    Ale to drobna kwestia, więc -> 2.5 / 3.0

b)  Logika jest jak najbardziej prawidłowa, ale dało się ją dużo bardziej uprościć ;)

    Mogłeś zrobić w skrócie:

    if WARUNEK_1 and WARUNEK_2 and WARUNEK_3:
        return True
    return False

    albo nawet: return WARUNEK_1 and WARUNEK_2 and WARUNEK_3

    Przyczepię się natomiast, że miałeś wypisać listę ocen, a nie średnią, ale ogólnie konieczność
    policzenia średniej mogła być nieco myląca, więc nie utnę Ci nic za to ;)

    Ocena za b: 2.0 / 2.0 (ale proszę uważać na czystość kodu i treść zadania!)

    

c)  Obiekt testowy spoko, tylko nazwa Szczepana powinna być z małej litery i dodawałeś przecinek
    po ostatniej ocenie w wywołaniu klasy (linijka 40)
    Poza tym spoko -> 0.5 / 1.0

d)  Nie ma komentarzy, ale type hinting bez zastrzeżeń -> 1.0 / 2.0

e)  Parę uwag:
        - (-0.5p)Całość powinna być sprawdzana w konstruktorze, nie w przestrzeni ogólnej klasy 
        - (-1p) Nie możesz sprawdzać w ten sposób warunku!

            Zgodnie z obecną logiką: self.ocena_informatyka or self.ocena_matma or self.ocena_wf != 2.0 or 3.0 or 3.5 or 4.0 or 4.5 or 5.0
            Wyrażenie zwraca TRUE, jeśli:

                - self.ocena_informatyka (nie ma porównań więc sprawdzamy czy jest różna od 0) LUB
                - self.ocena_matma (nie ma porównań więc sprawdzamy czy jest różna od 0) LUB
                - self.ocena_wf jest różna od 2.0 (cokolwiek innego niż 2.0 wyrzuci False) LUB
                - 3.0 (różne od 0 więc zawsze prawda)
                - 3.5 (różne od 0 więc zawsze prawda)
                - itd

            Poprawny i najprostszy sposób to utworzyć listę ocen lista_ocen = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0] i sprawdzić dla każdej oceny:
            self.ocena in lista_ocen

        - Rzucenie wyjątku OK... ale nie powinien to być wyjątek typu NameError i treść zamiast 'Error 400' powinna 
          mówić, skąd jest błąd ;)

    Ocena za e: 1.5 / 3.0

    Zadania rozwiązane fajnie, natomiast proponuję Ci poćwiczyć wyrażenia logiczne. Jeśli dam radę,
    to utworzę Wam jakiś mały zestaw do poćwiczenia - to Twój słaby punkt, poza tym radzisz sobie
    bardzo dobrze ;)

    Sumaryczna ocena: 7.5 / 11.0 -> ⭐➕
"""