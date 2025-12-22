QUIZ: 1 poprawna odpowiedź - 5 pkt

1. `15 pkt` Utwórz zmienną i wczytaj do niej wartość za pomocą funkcji `input()`. Następnie przekonwertuj tę zmienną na liczbę całkowitą. 

2. `25 pkt` Utwórz dwie zmienne: `a` i `b`. Następnie policz i wypisz funkcją `print()` pole i obwód prostokąta o bokach równych a i b. 

3. `40 pkt` Zapytaj użytkownika o jego wiek i na tej podstawie wyświetla w konsoli jeden z
komunikatów:
- Jesteś pełnoletni/a
- Nie jesteś jeszcze pełnoletni/a. Brakuje Ci XX lat do 18 roku życia
Zamiast XX powinna pojawić się wartość liczbowa

4. `40 pkt` Cena atrakcji turystycznej zależy od miesiąca. Napisz program, który zapyta użytkownika o liczbę biletów oraz miesiąc, w którym chce odwiedzić park rozrywki i na tej podstawie obliczy koszt transakcji.
Koszt biletu w danym miesiącu (miesiąc jako numer -> koszt biletu):
- 1 -> 50 zł
- 2 -> 50 zł
- 3 -> 100 zł
- 4 -> 100 zł
- 5 -> 200 zł
- 6 -> 200 zł
- 7 -> 250 zł
- 8 -> 200 zł
- 9 -> 200 zł
- 10 -> 100 zł
- 11 -> 100 zł
- 12 -> 50 zł
Wyświetl komunikat:
"Cena biletów: XX zł"

XX to wartość liczbowa

Jeśli wprowadzono niepoprawny numer miesiąc program powinien wyświetlić informację:
"Wprowadzono niepoprawny numer miesiąca. Spróbuj ponownie"

5. `30 pkt` Napisz program, który zapyta użytkownika o liczbę, a następnie wypisze na ekranie tyle wyników z rzutu kością sześcienną. Rzut kością sześcienną to wynik z losowania liczby od 1 do 6 (włącznie).

_Wskazówka: skorzystaj z instrukcji `from random import randint` aby wczytać funkcję `randint()`!_

Bonus `10 pkt`: Przy wyrzuceniu maksymalnej liczby oczek program powinien w tej samej linijce wypisać "TRAFIENIE KRYTYCZNE!"

6. `30 pkt` Napisz funkcję, która przyjmuje 2 argumenty:
- tekst, typu str
- n, typu int
i zwraca nowy napis, który powstaje poprzez połączenie text n razy.

Szablon funkcji:
```py
def laczenie_slow(): # Wstaw odpowiednie argumenty do tej funkcji!
nowy_tekst = ""
# Tu wstaw implementację
return # Tu wstaw co zwracasz
```

Bonus `10 pkt`: Dodaj type hinting i komentarze do definicji funkcji