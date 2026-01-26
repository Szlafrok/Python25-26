# MECHANIZM SLICINGU

lista = [2, 4, 6, 8, 10]

print(lista[3])

print(lista[1:4]) # indeksy 1, 2, 3 -> range(1, 4)

print(lista[0:2]) # -> [2, 4]

print(lista[1:5000]) # -> [4, 6, 8, 10]

print(lista[:3]) # -> [2, 4, 6]

print(lista[2:]) # -> [6, 8, 10]

print(lista[:]) # -> kompletna lista

# INDEKSY UJEMNE
print("-------------")

lista = [2, 4, 6, 8, 10]

print(lista[-1])
print(lista[-4])
print(lista[-5])
# print(lista[-5:-1]) # -> [2, 4, 6, 8]
# print(lista[-5:5]) # -> tak samo jak lista[-5:0] albo lista [-5:]

# IN

lista = [2, 4, 6, 8, 10]

if 2 in lista:
    print("2 jest w liście")
    
if 3 in lista:
    print("3 jest w liście")
else:
    print("3 nie jest w liście")