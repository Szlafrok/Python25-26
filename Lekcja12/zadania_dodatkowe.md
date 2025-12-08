# Termin wysłania zadań: 8.01.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

Na ten moment nie będziemy realizować dodatkowych zadań z Pygame. Zamiast tego powtórzymy funkcje!
Aby zdobyć bonusy, potrzebujemy:
| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 5 pkt |
| ⭐➕ | 6.5 pkt |
| ⭐➕➕ | 8 pkt |
| ⭐➕➕➕ | 9 pkt |

### Zadanie L12-1 `3 pkt` (ale można zdobyć do 5)

Zaproponuj własne zadanie programistyczne, które wymaga stworzenia i użycia co najmniej jednej funkcji. Możesz korzystać z elementów, które nie pojawiły się jeszcze na zajęciach, o ile nie są zbyt zaawansowane.

Następnie rozwiąż wymyślone przez siebie zadanie.

Damian 5 pkt
---

### Zadanie L12-2 `3 pkt`

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

Damian 3 pkt
---

### Zadanie L12-3 `2 pkt`

Proszę napisać funkcję `cyfry(n)`, która przyjmuje jako argument liczbę naturalną `n` i zwraca jej sumę cyfr.

Przykład:
`cyfry(1235)` -> 1 + 2 + 3 + 5 = 11

Damian 2 pkt
---
