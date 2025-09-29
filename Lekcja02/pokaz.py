# Co to jest komentarz?
"""
A tutaj mam taki fajny komentarz
Taki wielolinijkowy
"""

zmienna = 15

print("zmienna")
print(zmienna)

zmienna_2 = "Kociak"

print(zmienna_2)

kociak = "koteł"

zmienna_3 = kociak
print(zmienna_3)


calkowita = 18
dziesietna = 12.4
tekst = "słowo"
prawda = True
falsz = False

print(type(calkowita)) # int (integer)
print(type(dziesietna)) # float (liczba zmiennoprzecinkowa)
print(type(tekst)) # str (string)
print(type(prawda)) # bool (boolean)

print("------------")
tekst = calkowita
print(type(tekst))

prawda = falsz
print(type(prawda))


toJestNazwaZmiennej = 1 # Camel Case
ToJestNazwaZmiennej = 2 # Pascal Case
to_jest_nazwa_zmiennej = 3 # Snake Case (przyjmujemy dla zmiennych)
TO_JEST_NAZWA_ZMIENNEJ = 4 # Upper Case (przyjmujemy dla stałych)

CZYNNIK = 100500100900

print(1 * CZYNNIK)
print(2 * CZYNNIK)
print(3 * CZYNNIK)
print(4 * CZYNNIK)
print(5 * CZYNNIK)



calkowita = 18
dziesietna = 12.4
tekst = "słowo"
logiczna = True

int()
float()
str()
bool()

konwersja = float(calkowita)
print(konwersja)