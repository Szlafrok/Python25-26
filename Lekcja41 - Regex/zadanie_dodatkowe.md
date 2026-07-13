## Legenda o Królu Bajtku i numerach PIESEL

a) W odległym królestwie Cyberanii Południowej dobry król Bajtek wybrał się na spacer po królestwie i zapisał numery PIESEL wszystkich obywateli swojego państwa, chcąc następnie zlecić ministrowi cyfryzacji postawienie bazy danych i stworzenie rozwiązań technologicznych, aby ułatwić mieszkańcom codzienne życie. Niestety pewien zły człowiek (straszny hultaj) dopisał do królewskiej listy numerów PIESEL inne ciągi znaków o błędnym formacie.
Poprawny format numeru PIESEL z tego królestwa ma format `XXXXX-XXXXXXl`, gdzie każdy znak X zastępuje jakąś cyfrę 0-9, a litera l zastępuje dowolną małą literę. Proszę napisać funkcję zgodnie z szablonem

```py
def bajtek_szuka_pieseli(PIESELE: list) -> list:
    res = []
    # miejsce na Twoją implementację
    return res
```
tak, aby zwracała listę poprawnych numerów PIESEL.
> Przykład
```diff
+   12345-678901a
-   12345-67890a        # za mało cyfr w drugim członie
+   00000-000000z
-   1234-567890a        # za mało cyfr w pierwszym członie
+   54321-123456m
+   11111-222222k
-   123456-789012a      # za dużo cyfr
-   ABCDE-123456z       # litery zamiast cyfr
```

b) Numery PIESEL obywateli z Wólki Rivskiej spełniają następujący warunek: sumy cyfr pierwszego i drugiego członu liczbowego PIESELu (rozdzielone pauzą) są sobie równe. Król Bajtek chce utworzyć dla tych osób opcję korzystania z ulg podatkowych, ponieważ robią najlepszą kremówkę w królestwie.
Proszę zaktualizować powyższą funkcję tak, aby zwracała listę krotek `(pesel, rivia)`, gdzie `pesel` to poprawny numer PIESEL obywatela, a `rivia` to flaga `True/False`, która ma wartość `True` wtedy i tylko wtedy, gdy obywatel pochodzi z Wólki Rivskiej

c) Proszę zmodyfikować główną część zadania, rozpatrując sytuację, gdy ostatni znak numeru PIESEL może być zarówno małą, jak i wielką literą.

Powodzenia! 😎