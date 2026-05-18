### Przy wykonywaniu tych zadań dozwolone jest korzystanie z narzędzi AI pod warunkiem zrozumienia własnego kodu.
Wykonanie i omówienie **dowolnego** zadania zalicza zestaw i daje gwiazdkę!

### Zadanie 1
Proszę napisać program, który losuje i podaje użytkownikowi losową liczbę z zakresu 1000. Proszę następnie napisać program, który będzie zgadywał tę liczbę, a my będziemy udzielać mu odpowiedzi w postaci "za mało" / "za dużo" / "tak", zależnie od tego, czy zgadnięta liczba jest mniejsza lub większa od wylosowanej liczby, lub poprawna.

Program powinien korzystać z algorytmu, który umożliwi mu zgadnięcie prawidłowej liczby w możliwie najmniejszej liczbie prób.

(Bonusowe: Proszę podać i uzasadnić, dla jakiej przykładowo wylosowanej liczby komputer będzie potrzebował najwięcej prób. Ile będzie potrzebował tych prób?)

### Zadanie 2
https://pl.wikipedia.org/wiki/Sortowanie_przez_wybieranie

Sortowanie przez wybór to typ sortowania, który działa w następujący sposób:

Wybieramy granice przedziału `low = 0` oraz `high = n - 1`. Z przedziału tablicy od low do high wybieramy element największy i zamieniamy go miejscami z elementem ostatnim. Zmniejszamy high o 1 i wybieramy element największy spośród nowego przedziału, z którego usunęliśmy poprzedni element największy. W ten sposób wybieramy kolejne elementy największe i układamy je po kolei od końca, uzyskując posortowaną rosnąco listę.

Proszę zaimplementować funkcję
```py
def selection_sort(arr: list) -> list:
    pass
```
która zwróci posortowaną listę `arr`. Program powinien wykorzystywać zapisaną na lekcji funkcję `find_max()` oraz algorytm sortowania przez wybór.