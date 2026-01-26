from random import randint                                  # importujemy funkcję losującą liczby

wynik_gracza = 0                                            # licznik punktów gracza
wynik_komputera = 0                                         # licznik punktów komputera

while wynik_gracza < 10 and wynik_komputera < 10:           # gramy, dopóki ktoś nie zdobędzie 10 punktów
    if randint(1, 2) == 1:                                      # losujemy 1 lub 2 – symulacja rzutu monetą
        rzut = "o"                                              # 1 oznacza orła
    else:
        rzut = "r"                                              # 2 oznacza reszkę
    
    odpowiedz = input("Orzeł czy reszka? [o/r]: ")              # gracz wpisuje swoją odpowiedź
    if odpowiedz == rzut:                                       # sprawdzamy, czy gracz zgadł
        wynik_gracza += 1                                           # gracz dostaje punkt
        print(f"Zgadłeś! {wynik_gracza}-{wynik_komputera}")         # pokazujemy aktualny wynik
    else:
        wynik_komputera += 1                                        # komputer dostaje punkt
        print(f"Pudło! {wynik_gracza}-{wynik_komputera}")           # pokazujemy aktualny wynik

# po wyjściu z pętli gra się kończy (ktoś ma 10 punktów)
