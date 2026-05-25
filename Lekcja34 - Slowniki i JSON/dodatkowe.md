### Przy wykonywaniu tych zadań dozwolone jest korzystanie z narzędzi AI pod warunkiem zrozumienia własnego kodu i odpowiedzenia na pytania przy oddawaniu.
Wykonanie i omówienie **dowolnego** zadania zalicza zestaw i daje gwiazdkę!

### Zadanie 1
Proszę napisać program, który za pomocą słownika zlicza i wypisuje liczbę wystąpień elementów w tablicy. Program powinien następnie wypisać element (lub elementy), których wystąpień było najwięcej.

Przykładowo, dla listy:
```py
[1, 2, "kebab", 3, 2, 2, 2, 1, 1, "ugabuga", "ugabuga", "ugabuga", "ugabuga"]
```
wypisuje
```py
{
    1: 3,
    2: 4,
    "kebab": 1,
    3: 1,
    "ugabuga": 4
}
Największą liczbę wystąpień miały:
2
ugabuga
```
Wskazówka: warto skorzystać z funkcji `max()`!

### Zadanie 2
Proszę napisać program, który pozwala rejestrować się nowym użytkownikom, lub logować się istniejącym.

Na początku użytkownik powinien wpisać `R`, jeśli chce się rejestrować, lub `L` jeśli chce się logować. Jeśli chce się rejestrować, jego login i hasło powinny zostać zapisane do pliku `loginy.json`, jeśli chce się logować, jego login i hasło powinny być porównane z zapisanymi w pliku `loginy.json`. Można dodać sprawdzanie poprawności danych, ale jest to opcjonalne.