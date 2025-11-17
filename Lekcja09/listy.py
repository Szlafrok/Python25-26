zakupy = ["lego", "balony", "najki", "adidasy", "gaming"]
#          0       1         2        3          4

print(zakupy)

# Lista jest INDEKSOWANA
print(zakupy[0])
print(zakupy[2])
print(zakupy[4])

# Lista jest MODYFIKOWALNA
zakupy[1] = 25
zakupy[3] = True

print(zakupy)
print("\n----------------\n")
dane_1 = [
    ["Adam", "Kowalski", 24],
    ["Patryk", "Pietrek", 32],
    ["Bogusław", "Rumian", 50]
]

print(dane_1[2])
print(dane_1[2][1])

dane_2 = [
    [47, 29, 88, 28],
    [32, 54, 90, 63],
    [91, 53, 58, 92],
    [18, 34, 78, 99]
]

# Proszę podać, co wypiszą polecenia:
print(dane_2[1])  # [32, 54, 90, 63]
print(dane_2[2][0]) # 91
print(dane_2[0][0]) # 47
print(dane_2[3][3]) # 99
#print(dane_2[2][4]) błąd

# -----------------------------------------

przyklad = [1, 2, 3, 4]

przyklad.append(5) # Dodaj na końcu listy
przyklad.append(8)

print(przyklad)
print( len(przyklad) ) # Długość (liczba elementów listy) -> tutaj 6.

oceny = []
