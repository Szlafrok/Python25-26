# Termin wysłania zadań: 30.11
### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)
---

### Zadanie L6-1 `3 pkt`
Otrzymujemy trzy liczby całkowite `a`, `b` oraz `c`. Można założyć, że będą one podane **w kolejności rosnącej, zatem liczba `c` będzie zawsze największa.**

Trójkąt można utworzyć, jeśli suma długości dwóch krótszych boków jest większa niż długość najdłuższego boku. Proszę napisać program, który wczytuje liczby `a`, `b` i `c` i określa, czy można utworzyć trójkąt z boków o takich długościach.

#### *Zadanie dodatkowe.* `+2 pkt`
Prosze przepisać ten program bez założenia, że liczba `c` zawsze będzie największa, tzn. kolejność liczb `a`, `b`, `c` nie jest określona.

---
### Zadanie L7-1 `4 pkt + 1 pkt` - Gra w większe i mniejsze
```py
from random import randint
# poniżej zapisz implementację programu
```
#### Część 1 (4p)
Funkcja `randint(a, b)` to funkcja zwracająca losową liczbę całkowitą z przedziału `[a, b]` (wliczając w to także same liczby a oraz b). Korzystając z tej funkcji proszę napisać program, który wylosuje dowolną liczbę z przedziału od 1 do 1000. Funkcję możesz zaimportować do programu powyższym poleceniem.
Program następnie powinien zacząć na zmianę prosić gracza o odgadnięcie liczby i wypisywać mu "za dużo" jeśli jego odpowiedź jest większa od oczekiwanej liczby, lub "za mało" jeśli jest mniejsza. Gra powinna dobiec końca w momencie, kiedy gracz odgadnie liczbę. Na końcu gry proszę pogratulować graczowi i podać liczbę prób odgadnięcia liczby.

#### Część 2 (1p)
Proszę opisać sposób, który pozwoli odgadnąć liczbę w możliwie najmniejszej liczbie prób. Jak nazywa się algorytm wykorzystywany przez tę metodę?

---