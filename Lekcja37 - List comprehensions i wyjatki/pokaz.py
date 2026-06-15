# Proszę za pomocą PROGRAMU utworzyć listę, która zawiera liczby od 1 do 100.

# - użyć pętli for
# - użyć range()
# - użyć metody .append()

lista = [] # 1 - 100

# for i in range(100): # 0 - 99
#     lista.append(i + 1)

for i in range(1, 101):
    lista.append(i)

print(lista)