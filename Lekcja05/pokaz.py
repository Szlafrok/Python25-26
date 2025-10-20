'''
To jest komentarz
Wielolinijkowy
'''

"""
A to...
TEŻ
"""

_zmienna = 5

# --------------------------------

poziom_baterii = 16

if poziom_baterii <= 15:
    print("Naładuj baterię!")
    print("Szukaj ładowarki!")
# koniec ifa

print("Wykonam się niezależenie")
print("-------")

dzielna = int(input("Wprowadź dzielną: "))
dzielnik = int(input("Wprowadź dzielnik: "))

if dzielnik == 0:
    print("Nie można wykonać dzielenia")
if dzielnik != 0:
    print(dzielna / dzielnik)