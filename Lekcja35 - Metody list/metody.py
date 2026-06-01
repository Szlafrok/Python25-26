lista = [5, 10, "chomik", 15, "szczur", 3, "wiewiórka"]

print(lista)


# append
lista.append(-3)
print(lista)

# extend
# slownik = {0: "ebe", 1: "ebe", 2: "bebe"}
# for elem in slownik:
#     print(elem) # iteracja po słowniku daje mi jego KLUCZE

a = [1, 2, 3]
b = [4, 5]

a.extend(b)
print(a)

b.extend(a)
print(b)