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

# insert
print("--- metoda insert ---")
lista = [1, 2, 3, 4, 5]

lista.insert(0, 10) # (indeks, wartosc)
print(lista)

# proszę utworzyć listę [2, 4, 6, 8, 10]
# następnie za pomocą poleceń insert proszę wstawiać elementy
# tak, aby kształt listy był następujący:

lista = [2, 4, 6, 8, 10]
# [2, 4, 6, 7, 8, 10]
lista.insert(3, 7)

# [0, 2, 4, 6, 7, 8, 10]
lista.insert(0, 0)
print(lista)
# [0, 2, 4, 6, 7, 8, 20, 10]
lista.insert(6, 20)
print(lista)
# [0, 2, 5, 4, 6, 7, 8, 20, 10]
lista.insert(2, 5)
print(lista)

print("--- remove ---")
lista_zakupow = ["kebab", "kajzerka", "kebab", "pepsi", "haribo", "lego batman"]

lista_zakupow.remove("kebab")
print(lista_zakupow)
lista_zakupow.remove("kebab")
print(lista_zakupow)


print("--- index ---")
lista = ["abc", "def", "ghi", "jkl", "mno", "pqr", "abc"]

print(lista.index("abc")) # 0
print(lista.index("mno")) # 4
print(lista.index("ghi")) # 2
print(lista.index("abc", 4)) # 6, bo pierwsze 'abc' zostaje zignorowane
# print(lista.index("KACZUCHA")) # błąd

print("--- pop ---")

lista = [10, 20, 30, 40, 50]
pobrane = lista.pop() # usuwa ostatni element
print(pobrane)

lista.pop(0) # usuwa pierwszy element
print(pobrane)



print("--- sort ---")
lista = [5, 0, 1, 3, 2]
lista.sort()
print(lista)


lista.reverse() # odwraca listę W MIEJSCU   
lista.copy() # kopiuje listę - KOPIA PŁYTKA
lista.clear()

# Dodatkowe: Proszę napisać odpowiednik metody REMOVE, 
# czyli usunięcie pierwszego wystąpienia wyrażenia w liście, 
# za pomocą metod POP i INDEX

# Bartek, Damian, Antek - +1 gwiazdka