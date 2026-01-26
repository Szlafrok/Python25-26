# Termin wysłania zadań: 8.02.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

Aby zdobyć bonusy, potrzebujemy:
| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 5 pkt |
| ⭐➕ | 7 pkt |
| ⭐➕➕ | 9 pkt |
| ⭐➕➕➕ | 11 pkt |
| ⭐➕➕➕➕ | 13 pkt |
| ⭐➕➕➕➕➕ | 14.5 pkt |

### Zadanie L15-1 `3 pkt
Liczba `4023123` może być w systemie liczbowym co najwyżej piątkowym, ponieważ występuje w niej cyfra 4. Nie może to być zatem system czwórkowy, ale system piątkowy, szóstkowy, siódemkowy, itd. już tak.

Proszę zaimplementować funkcję `minsys(n)`, która przyjmie ciąg cyfr `n` i zwróci najmniejszą podstawę systemu, w jakim może być zapisana ta liczba. Przykładowo, dla `4023123` najmniejszą podstawą systemu jest 5 (bo system piątkowy).

---

### Zadanie L15-2 `3 pkt`

Proszę zaimplementować funkcję trojeczka(n), która przyjmuje jako argument liczbę naturalną n zapisaną w systemie dziesiętnym i zwraca tę liczbę w systemie trójkowym. Przykładowo, dla wywołania:

```py
wynik = trojeczka(17)
print(f"Zadanie domowe 2: Wynik = {wynik}")
```
Otrzymanym wynikiem będzie "122" (bo 2*1 + 2*3 + 1*9 = 2 + 6 + 9 = 17)

---

Proszę napisać funkcję `perfect(n)`, która przyjmuje liczbę naturalną `n` jako argument i zwraca

- `True`, jeśli `n` jest liczbą doskonałą
- `False`, jeśli `n` nie jest liczbą doskonałą

---

### Zadanie L15-3 `5 pkt`

SZABLON:
```py
def cwaniak(wyrazy: list) -> int:
    n = len(wyrazy) # Długość listy wyrazy - liczba słów
    cwane = [False] * n # Określa, które wyrazy są cwane
    pass # Tu proszę wpisać dalszy ciąg funkcji!
```

W liście wyrazy zawarta jest pewna liczba słów zapisanych w formacie stringa. Dane słowo jest cwane, jeżeli w tej liście znajduje się słowo zapisane w odwrotnej kolejności liter. Przykładowo, wyraz "majster" jest cwane, jeżeli na tej liście znajduje się wyraz "retsjam". Palindromy są cwane i mogą łączyć się same ze sobą!

Proszę zaimplementować funkcję **`cwaniak(wyrazy)`**, która przyjmuje jako argument listę `wyrazy` i zwraca liczbę CWANYCH słów z tej listy.

Przykład. Dla wywołania:
```py
wynik = cwaniak(["kot", "kot", "pies", "pies", "owocowo", "tok"])
print(f"Zadanie dodatkowe L15-2: Wynik = {wynik}")
```
do zmiennej wynik zostanie zwrócona liczba 4. Uzasadnienie:

```py
cwaniak[0] == "kot". #Odwróceniem tego wyrazu jest "tok", a "tok" jest obecne na tej liście. "kot" jest cwany! (1)
cwaniak[1] == "kot". #Odwróceniem tego wyrazu jest "tok", a "tok" jest obecne na tej liście. "kot" jest cwany! (2)
cwaniak[2] == "pies". #Odwróceniem tego wyrazu jest "seip", a "seip" nie ma na tej liście. "pies" NIE jest cwany!
cwaniak[3] == "pies". #Odwróceniem tego wyrazu jest "seip", a "seip" nie ma na tej liście. "pies" NIE jest cwany!
cwaniak[4] == "owocowo". #Odwróceniem tego wyrazu jest "owocowo", a "owocowo" jest obecne na tej liście. "owocowo" jest cwane! (3)
cwaniak[5] == "tok". #Odwróceniem tego wyrazu jest "kot", a "kot" jest obecne na tej liście. "tok" jest cwany! (4)
```

WSKAZÓWKI:
1. Proszę skorzystać z implementacji z lekcji, która sprawdza, czy wyraz jest palindromem. Przyda się ;)
2. Warto będzie skorzystać z pętli for, a nawet dwóch.
3. Oznaczaj cwane wyrazy jako True w liście "cwane"! Suma wszystkich elementów listy zawierającej wartości typu `bool` jest równa liczbie elementów o wartości `True`, bo `True` jest równe 1!

---

### Zadanie L15-4 `4 pkt`
Rozkład liczby N na czynniki pierwsze to rozkład liczby na iloczyn taki, że wszystkie liczby rozkładu przemnożone przez siebie dają liczbę początkową N, oraz każda liczba rozkładu jest liczbą pierwszą.

Proszę zaimplementować funkcję `prime_factors(n)`, która przyjmie jako argument liczbę naturalną dodatnią `n` i zwróci listę jej czynników pierwszych.

Przykład. Dla wywołania
```py
n = 240
print(prime_factors(n))
```
wynikiem będzie `[2, 2, 2, 2, 3, 5]`, bo 2 * 2 * 2 * 2 * 3 * 5 = 240 oraz 2, 3, 5 to liczby pierwsze.

*Uwaga. W tym zadaniu dozwolone jest swobodne korzystanie z pomocy zewnętrznych oraz AI, ale aby zaliczyć zadanie, należy zgłosić się po zajęciach i o nim opowiedzieć!*