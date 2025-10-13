# Termin wysłania zadań: 31.10


### Zadanie L3-1 `3 pkt`

(a) Proszę pobrać od użytkownika imię, nazwisko, rok urodzenia i wypisać do terminalu informację o jego imieniu, nazwisku i wieku. Należy wykorzystać w tym celu fstringa. Do zbierania danych od użytkownika używamy funkcji input() `2.5 pkt`

*Przykład.* Dla danych:
```py
imie = "Jan"
nazwisko = "Kowalski"
rok_urodzenia = 1996
```

Powinniśmy otrzymać napis:
```py
"Jan Kowalski ma 29 lat."
```

(b) Proszę wykonać to zadanie tak, żeby nie tworzyć specjalnie nowej zmiennej na wiek przed wstawieniem danych do funkcji print(). `0.5 pkt`


### Zadanie L3-2 `3 pkt`

Proszę napisać program, który zapyta i pobierze od użytkownika dwie liczby, a następnie poda wynik dzielenia z resztą, podając ILORAZ oraz RESZTĘ. Należy w tym celu użyć fstringa. Do zbierania liczb od użytkownika używamy funkcji input()

Dla danych:
```py
dzielna = 48
dzielnik = 10
```
powinniśmy otrzymać napis:
```py
"48 dzielone przez 10 jest równe 4 i daje 8 reszty."
```

### Zadanie L4-1 `2 pkt`

Określ czy obecna pora dnia i pogoda nadaje się na wyjście z domu. 
Zmienna `pogoda` przyjmuje napisy odpowiadające aktualnej pogodzie: “słonecznie”, “pochmurnie”, “deszczowo”, “burzowo”.
Zmienna `godzina` przechowuje obecną godzinę (0 - 23)

Zmienna typu bool czy_mozna_wyjsc powinna przyjąć wartość True, jeśli na dworze jest słonecznie i jest między 9, a 19 lub jest pochmurnie i jest między 9 a 15. W przeciwnym razie powinna przyjąć wartość False. Uzupełnij poniższy szablon.
```py
godzina = int(input())
czy_mozna_wyjsc = #Uzupełnij wyrażenie logiczne
print(czy_mozna_wyjsc)
```