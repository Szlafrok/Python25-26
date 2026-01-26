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

# dzielna = int(input("Wprowadź dzielną: "))
# dzielnik = int(input("Wprowadź dzielnik: "))

# if dzielnik == 0:
#     print("Nie można wykonać dzielenia")
# else:
#     print(dzielna / dzielnik)


# if 10 <= wiek <= 99:
#     print("Ten zestaw klocków jest dla ciebie!")
# else:
#     print("Ten zestaw klocków nie jest dla ciebie!")

wiek = int(input("Podaj wiek: "))

if 10 <= wiek <= 99:
    print("Ten zestaw klocków jest dla ciebie!")
elif wiek < 10:
    print("Jesteś za młody!")
else:
    print("Jestes za stary!")


liczba = int(input())

if liczba == 0:
    print("Liczba jest zerowa")
elif liczba > 0:
    print("Liczba jest dodatnia")
elif liczba < 0: # else
    print("Liczba jest ujemna")