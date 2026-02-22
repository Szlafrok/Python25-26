# Termin wysłania zadań: 8.03.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

Aby zdobyć bonusy, potrzebujemy:
| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 4.5 pkt |
| ⭐➕ | 6.5 pkt |
| ⭐➕➕ | 7.5 pkt oraz uporządkowany i czytelny kod 😉 |

### Zadanie 1 `2 pkt`
Proszę dodać postaci podczas ataku szansę na trafienie krytyczne (zadanie 5 obrażeń zamiast 0-3)

### Zadanie 2 `2 pkt`
Proszę wymyślić swojemu bohaterowi klasę postaci i utworzyć mu trzeci ruch oprócz "atak" i "uciekaj", np. medyk - uzdrowienie, pirotechnik - podpalenie. Można zdobyć dodatkowy punkt za dodanie efektu statusu lub ograniczenia ataku, np. atak podpala przeciwnika i przez 3 kolejki zadaje mu obrażenia, lub danego ataku można użyć tylko raz na walkę ;)

### Zadanie 3 `5 pkt`
W konstruktorze Postaci proszę utworzyć zmienną przechowującą dla każdej postaci złoto. Wartość początkowa złota powinna wynosić losowo od 1 do 20. Wiedząc, że funkcja `random.randint(a, b)` losuje dowolną liczbę całkowitą od `a` do `b` włącznie, proszę zmodyfikować logikę gry:
- Pokonanie przeciwnika daje graczowi jego złoto
- Gracz podczas zwiedzania świata ma 40% szans na znalezienie jaskini, 40% szans na walkę z wrogiem i 20% szans na znalezienie skarbu, który zapewnia premię od 20 do 50 sztuk złota
- Gracz może zamiast zwiedzania lub odpoczynku zakupić za 30 sztuk złota apteczkę, która leczy go o 50% maksymalnego zdrowia
