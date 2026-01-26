# Termin wysłania zadań: 8.02.2026

### Zasady i sposób wysyłania zadań: [LINK](https://github.com/Szlafrok/Python25-26/blob/main/Zasady%20i%20informacje/zasady_zadan.md)

---

Aby zdobyć bonusy, potrzebujemy:
| Nagroda | Minimalny wynik |
| ------- | --------------- |
| ⭐ | 6 pkt |
| ⭐➕ | 8 pkt |
| ⭐➕➕ | 9 pkt |
| ⭐➕➕➕ | 10 pkt |

### Zadanie L16-1 `3 pkt`
Korzystając z przygotowanego w czasie lekcji projektu w pliku projekt.py proszę zaimplementować limit salda konta. Limit powinien być ustawiany za pomocą stałej:

```py
LIMIT = 1200 # Przykładowa wartość
```
Podczas wpłaty pieniędzy na konto saldo nie może przekroczyć limitu. Rozwiązanie proszę opatrzyć komentarzami i przesłać cały projekt 😉

---

### Zadanie L16-2 `3 pkt`

Dana jest funkcja, która pobiera i zwraca dane logowania:

```py
def pobierz_pin() -> str: # Zwraca wprowadzony kod PIN w formie stringa
    kod_pin = input("Wprowadź PIN do karty: ")
    return kod_pin 
```

Podobnie jak w zadaniu 1, proszę przyjąć, że obecna jest stała:
```py
PIN = "1234" # Przykładowe dane
```

Proszę przeprogramować projekt tak, aby przed przyznaniem dostępu do menu głównego pytał się użytkownika o kod PIN. Program powinien dopuszczać dwa błędy, przy trzecim powinien zakończyć działanie. Podanie poprawnego pinu przenosi nas do wyboru operacji.

---

### Zadanie L15-3 `1 pkt`

Proszę przepisać zadanie L15-2 tak, aby dopuszczało N prób logowania zamiast trzech. N powinno być określone w stałej, podobnie jak PIN i LIMIT.

---

### Zadanie L15-4 `3 pkt`

Proszę zaimplementować piątą opcję wyboru dla użytkownika - historię operacji na koncie. Każdy wpis w historii powinien zawierać informacje o typie operacji (wpłata/wypłata), jej kwocie oraz saldzie po wykonanej operacji. Można wykorzystać do pomocy poniższy skrypt:
```py
historia = [
            (1, 50, 50),
            (2, 30, 20)
                        ] # Przykładowe dane

for wpis in historia:
    if wpis[0] == 1:
        print(f"Wpłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")
    else:
        print(f"Wypłata {wpis[1]} zł - obecne saldo {wpis[2]} zł.")
```