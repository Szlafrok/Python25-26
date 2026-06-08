zbior = {1, 2, 3, 3}
krotka = (4, 5, 6)
lista = [7, 8, 8, 9]

print(len(zbior))
print(len(krotka))
print(len(lista))

print(3 in zbior)
print(3 in krotka)
print(3 in lista)

print("Zbiór na listę")
konwersja = list(zbior)
print(konwersja)
print(type(konwersja))

print("Lista na krotkę")
konwersja = tuple(lista)
print(konwersja)
print(type(konwersja))

print("Lista na zbiór")
konwersja = set(lista)
print(konwersja)
print(type(konwersja))

for element in zbior:
    print(element)