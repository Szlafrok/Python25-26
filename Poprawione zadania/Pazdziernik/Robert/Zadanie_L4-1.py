print("Wybierz jaka jest pogoda")
pogoda = input("[s]lonecznie / [p]ochmurnie / [d]eszczowo / [b]urzowo : ")

if (not (pogoda == "s" or pogoda == "p" or pogoda == "d" or pogoda == "b")):
    print(f"Wybierz poprawna pogode (podano: {pogoda})")
else:
    godzina = int(input("Podaj godzine: "))
    czy_mozna_wyjsc = (pogoda == "s" and godzina >= 9 and godzina <= 19) or (pogoda == "p" and godzina >= 9 and godzina <= 15) 
    print(czy_mozna_wyjsc)

    if (czy_mozna_wyjsc):
        print("Mozna wyjsc! Udanego spaceru.")
    else:
        print("Poczekaj na lepsza pogode...")

"""
Zadanie bardzo fajnie rozbudowane! Bazowo nie znaliśmy instrukcji if/elif/else na 4 lekcji, ale dzięki Twoim dodatkom
program jest dużo bardziej czytelny dla użytkownika. Wczytanie danych poprawne i rdzeń zadania (wyrażenie logiczne sprawdzające
czy możemy iść na dwór) są prawidłowe.

Rozwiązanie jest super, mogę jedynie podsunąć tu parę uwag, w ramach ciekawostek:
- Informacja "poczekaj na lepszą pogodę" wyświetla się także, jeśli pogoda jest OK, ale jest za wcześnie lub za późno
- Operator AND wiąże wyrażenia mocniej, niż operator OR. Mówimy tu o kolejności wykonywania działań: najpierw wykonujemy
  operacje AND (tak jak mnożenie w matematyce), a następnie operacje OR (tak jak dodawanie). Innymi słowy, dodanie nawiasów
  nie zmieniło logiki Twojego kodu... ale na pewno dodało mu czytelności!
- Wyrażenie "godzina >= 9 and godzina <= 19" można połączyć: "9 <= godzina <= 19".

3 / 3p 😉
Gratulacje!
"""