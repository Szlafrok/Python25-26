lista = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6]
#        0     2     4     6     8
# x podzielne przez 2:
# x % 2 == 0:

# Proszę napisać program, który wypisze z listy wyłącznie elementy które
# leżą na PARZYSTYCH indeksach.

# Dla powyższej listy powinniśmy otrzymać:
# 5, 3, 1, 9, 7

# Nalezy użyć pętli for, na przykład:

# Program wypisujący wartości większe od 4 z listy:
for i in range(10):
    if lista[i] > 4:
        print(lista[i])

print("-----")

for i in range(10):
    if i % 2 == 0:
        print(lista[i])