from random import randint

powt = int(input())

lista = []
for i in range(powt):
    lista.append(randint(1, 100))

print(lista)