# Termin wysłania zadań: 7.12

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

### Zadanie L6-1 `3 pkt`

Otrzymujemy trzy liczby całkowite `a`, `b` oraz `c`. Można założyć, że będą one podane **w kolejności rosnącej, zatem liczba `c` będzie zawsze największa.**

Trójkąt można utworzyć, jeśli suma długości dwóch krótszych boków jest większa niż długość najdłuższego boku. Proszę napisać program, który wczytuje liczby `a`, `b` i `c` i określa, czy można utworzyć trójkąt z boków o takich długościach.

#### _Zadanie dodatkowe._ `+2 pkt`

Prosze przepisać ten program bez założenia, że liczba `c` zawsze będzie największa, tzn. kolejność liczb `a`, `b`, `c` nie jest określona.

---

### Zadanie L7-1 `1 pkt`

Proszę opisać sposób z gry "Gra w większe i mniejsze" z lekcji, który pozwoli odgadnąć liczbę w możliwie najmniejszej liczbie prób. Jak nazywa się algorytm wykorzystywany przez tę metodę?

## Projekt P1 `8 pkt` - "Matematyczne Combosy 📚💻

Proszę napisać grę zadającą użytkownikowi losowe pytania matematyczne. Gra powinna składać się z czterech rund. Trzy pierwsze rundy powinny dotyczyć (proszę wybrać 3 elementy):

- Dodawania
- Odejmowania
- Mnożenia
- Potęgowania

  Ostatnia, finałowa runda, powinna dotyczyć (proszę wybrać 1 element)

- Dzielenia całkowitego
- Dzielenia zwykłego
- Reszty z dzielenia

Gracz kończy grę po ukończeniu wszystkich rund. Ukończenie rundy wymaga udzielenia poprawnych odpowiedzi na 5 pytań z rzędu.
Do losowania pytań można zaimportować i wykorzystać polecenie:

```py
from random import randint # import polecenia
losowe = randint(1, 10) # Losuje losową liczbę od 1 do 10 (1 i 10 też mogą wypaść)
```

Bonus: Polecenie

```py
from time import time # import polecenia
czas_startu = time()
```

pozwala zapisać aktualny czas w sekundach. Proszę uzupełnić projekt o zliczanie czasu - pomiar rozpoczyna się na początku, a wartość czasu jest wypisywana po ukończeniu gry.
_Można posiłkować się pomocami, ale mogę zadać pytanie lub dwa o projekt pod koniec zajęć 😉_

Punktacja:

Poprawne pierwsze trzy rundy: `3 pkt`

Poprawna runda finałowa: `2 pkt`

Porządek i struktura kodu: `2 pkt` (warto dodać komentarze!)

Interfejs użytkownika (jasne komunikaty): `1 pkt`

Zrealizowanie zadania bonusowego: `+1 pkt`

_Projekt z najwyższą oceną, jeśli autor wyrazi taką chęć, będzie pokazany na lekcji!_ 🏆

---

### Zadanie L8-1 `4 pkt`

Proszę napisać program, który zapyta użytkownika o wysokość (liczbę linijek), a następnie wyświetli choinkę / piramidę o podanej wysokości. Choinka ma składać się z gwiazdek (\*) oraz spacji jako znaków białych.
Przykładowa choinka dla wysokości równej 4: (znak o oznacza spację)

```
o o o *
o o * o *
o * o * o *
* o * o * o *
```

---

### Zadanie L8-2 `4 pkt`

Proszę napisać program, który wczyta od użytkownika dwie liczby: wysokość i szerokość, a następnie wypisze w konsoli prostokąt składający się z kwadratów (■). Program powinien mieć dwa tryby, spośród których użytkownik może wybrać: prostokąt ma być pusty lub pełny w środku.
Przykład: dla danych

```py
czy_pusty = True
wysokosc = 3
szerokosc = 4
```

Otrzymamy prostokąt:

```
■■■■
■  ■
■■■■
```

_Podpowiedź: Proszę wykorzystać mnożenie stringów._

---

### Zadanie L9-1 `3 pkt`
Proszę napisać program, który odwraca kolejność elementów dowolnej listy i wypisuje ją zgodnie z szablonem:
```py
lista_a = [-5, -3, 1, 5, 100]
lista_b = []
# Kod odwracajacy liste "lista_a" wpisz ponizej



# Pokaz obie listy
print(lista_a)
print(lista_b) # Oczekiwane dla tych danych: [100, 5, 1, -3, 5]
```

---

### Zadanie L10-1 `1 pkt`
Proszę napisać funkcję, która przyjmie jako argumenty boki prostokąta `a` oraz `b` i wypisuje do konsoli jego pole.

### Zadanie L10-2
Proszę napisać funkcję `join(lacznik, teksty)`, która przyjmuje jako argumenty:
- stringa `lacznik`
- listę stringów `teksty`
i wypisuje pojedynczy ciąg złożony z kolejnych elementów listy teksty, połączonych pomiędzy sobą łącznikami.

Przykłady:

- `join("/", ["bardzo", "lubię", "ciastka"])` -> `"bardzo/lubię/ciastka"`
- `join("-", ["i have", "your food", "sir"])` -> `"i have-your food-sir"`
- `join("%", ["pojedynczy element"])`         -> `"pojedynczy element"`

*Wskazówka: argument `end = ""` w funkcji print() może być przydatne w jednym ze sposobów rozwiązania.*
**W tym zadaniu nie wolno korzystać z wbudowanej metody stringów .join()! Skrypt należy napisać samodzielnie.**