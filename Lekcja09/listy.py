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

