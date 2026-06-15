krotka = tuple(x for x in range(10))
print(krotka)

zbior = {x for x in range(10)}
print(zbior)


lista = [0, 0, 0, 0, 0, 0, 0, 1]
zbior = {x for x in lista}
print(zbior)

imiona = ["Antek", "Ola", "Damian", "Gabriel", "Maks", "Bartek", "Wojtek", "Piotrek"]

slownik = {imie : len(imie)+1 for imie in imiona}
print(slownik)

for k, v in slownik.items():
    print(k, v)