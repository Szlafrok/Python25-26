def hejka():
    print("Hejka!", end = " ")
    print("Kaczkowróbel je kebaba i zabił nim gołombiodziobaka")
    print("bo miał jajo z roleksem")

hejka()

def dodaj(a, b):
    print(a + b)

dodaj(5, 8)
dodaj(11, 9)

def sumuj_elementy(lista):
    wynik = 0
    for elem in lista:
        wynik += elem
    print(wynik)

lista1 = [2, 4, 5]
lista2 = [6, 7, 8, 9]
lista3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]

sumuj_elementy(lista1)

sumuj_elementy(lista2)

sumuj_elementy(lista3)

def wypisz_wymaluj(wyraz, powtorzenia):
    for i in range(powtorzenia):
        print(wyraz)

wypisz_wymaluj("wrunel drwal z maka wieś mac", 5)

# def print(): TAK NIE ROBIMY!!!!!!!!!!!!!!!!!!!
# print = 5 TAK TEŻ NIE ROBIMY !!!!!!!!!!!!!!!!!!    

"""
    ZADANIE SAMODZIELNE!

    Proszę napisać funkcję, która przyjmie jako argument
    bok kwadratu a i policzy jego obwód
"""

def obwod_protokata(a, b):
    print(2*a + 2*b)

obwod_protokata(2, 3)

def obwod_kwadratu(a):
    print(4*a)