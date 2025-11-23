# Termin wysłania zadań: 8.01.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---
### Zadanie L11-1 `3 pkt` (ale można zdobyć do 5)
Zaproponuj własne zadanie programistyczne, które wymaga stworzenia i użycia co najmniej jednej funkcji. Możesz korzystać z elementów, które nie pojawiły się jeszcze na zajęciach, o ile nie są zbyt zaawansowane.

Następnie rozwiąż wymyślone przez siebie zadanie.

---

### Zadanie L11-2 `3 pkt`
Dana jest funkcja:
```py
def logowanie(popr_login, popr_haslo):
    login = input("Podaj login: ")
    haslo = input("Podaj hasło: ")
    if login == popr_login and haslo == popr_haslo:
        return True
    return False
```
Przepisz funkcję tak, aby przyjmowała dodatkowy argument `n`, oznaczający liczbę dopuszczalnych prób logowania.

Funkcja powinna zwrócić:
- `True`, jeśli użytkownik poprawnie się zaloguje,
- `False`, jeśli wykorzysta wszystkie próby i dalej nie poda poprawnych danych.

---

### Zadanie L11-3 `2 pkt`
Proszę napisać funkcję `cyfry(n)`, która przyjmuje jako argument liczbę naturalną `n` i zwraca jej sumę cyfr.

Przykład:
`cyfry(1235)` -> 1 + 2 + 3 + 5 = 11

---

### Zadanie L11-4 `3 pkt`
Liczba doskonała to taka liczba, która jest równa sumie jej dzielników mniejszych od niej.
Przykład. Liczba 28 jest doskonała, bo:
- Dzielniki 28, które są mniejsze od tej liczby, to `14, 7, 4, 2, 1`
- 14 + 7 + 4 + 2 + 1 = 28

---

Proszę napisać funkcję `perfect(n)`, która przyjmuje liczbę naturalną `n` jako argument i zwraca
- `True`, jeśli `n` jest liczbą doskonałą
- `False`, jeśli `n` nie jest liczbą doskonałą

---

### Zadanie L11-5 `3 pkt`
Proszę uzupełnić rozwiązania wszystkich powyższych zadań o type hinting oraz komentarze wyjaśniające działanie programów ;)

---

### Zadanie L13-1 `2 pkt`
Proszę dodać do projektu funkcję sprintu - kiedy gracz trzyma klawisz shift, powinien poruszać się dwa razy szybciej.

---

*Zostaną dodane 1-3 zadania z lekcji 15 - będzie to bliżej terminu zajęć!*