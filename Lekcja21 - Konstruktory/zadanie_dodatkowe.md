# Termin wysłania zadań: 8.02.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

Aby zdobyć bonusy, potrzebujemy:
| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 6 pkt |
| ⭐➕ | 8 pkt |
| ⭐➕➕ | 10 pkt |
| ⭐➕➕➕ | 11 pkt |

### Zadanie dodatkowe
Proszę napisać klasę Student, która w swoim konstruktorze:

#### a) (3 pkt)
- wczyta wartości:
    - nazwisko, wyrażające się jako tekst
    - ocena_matematyka, ocena_informatyka, ocena_wf, wyrażające się jako liczby zmiennoprzecinkowe (dziesiętne)
- wyznaczy średnią ocen studenta (podstawi do wartości self.srednia)
- określi, czy student zaliczył wszystkie przedmioty (ocena z każdego przedmiotu musi wynosić 3.0 lub wyżej)

#### b) (2 pkt)
Następnie proszę zaimplementować metody:
- wypisz_oceny(self), która wypisze oceny studenta
- zdane(self), która powie, czy student zaliczył wszystko czy nie

#### c) (1 pkt)
Proszę utworzyć odpowiedni obiekt z testowymi danymi, a następnie
przetestować metody.


#### d) (2 pkt)
Proszę uzupełnić kompletny type hinting oraz komentarze dotyczące poszczególnych elementów klasy.

#### e) (3 pkt)
Proszę skorzystać z polecenia `raise` ([Link](https://docs.python.org/pl/3/tutorial/errors.html#raising-exceptions)), aby przerwać program i rzucić wyjątek, jeśli podczas tworzenia obiektu zostanie wprowadzona ocena poza dopuszczalną skalą. Dopuszczalna skala ocen to: 2.0, 3.0, 3.5, 4.0, 4.5, 5.0.