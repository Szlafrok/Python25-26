
#zadanie L3-1
imie = input("wprowadź imię:  ")
nazwisko = input("wprowadź nazwisko:  ")
rok_urodzenia = int(input("wprowadź rok urodzenia:   "))

print(f"{imie} {nazwisko} ma {2025-rok_urodzenia} lat")

# Super elegancko B)
# (3 / 3)


#zadanie L3-2
dzielna = int(input("podaj dzielną: "))
dzielnik = int(input("podaj dzielnik:  "))
iloraz = dzielna // dzielnik
reszta = dzielna % dzielnik
print(f"{dzielna} dzielone przez {dzielnik} jest równe {iloraz} i daje {reszta} reszty.")

# Super!
# (3 / 3)

#zadanie L4-1
godzina = int(input("Podaj godzinę:  "))
pogoda = str(input("Jak jest na dworze?:  "))
pogoda = pogoda.lower()
czy_mozna_wyjsc = 9 < godzina < 19 and pogoda == "słonecznie" or 9 < godzina < 15 and pogoda == "pochmurnie"
print(czy_mozna_wyjsc)

# Fajne, eleganckie rozwiązanie
# Widzę, że zauważyłes, że AND wiąże wyrażenia mocniej, niż OR ;)
# (3 / 3)


# Proszę od następnego razu dodawać rozszerzenie pliku .py ;)