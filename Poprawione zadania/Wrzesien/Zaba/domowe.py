#ZADANIE L1-1
# Pseudonim - Żaba

# (2p)

# ZADANIE L1-2
# Widziałem Cię na discordzie :) (+2p)

#ZADANIE L2-1

int()#liczba całkowita
float()#ułamek dziesiętny
str()#tekst
bool()#True/False

zmienna = float("19.09")
print(zmienna + 2.28)#21.37

# a.int -> str - działa zawsze (zamienia liczbę na tekst)
a = str(36)
print(a) # +

# b.float -> str - działa zawsze (zamienia liczbę na tekst)
b = str(7.6)
print(b) # +

# c.str -> bool - działa zawsze i wychodzi zawsze True (z wyjątkiem kiedy nic nie wpiszemy, wtedy wychodzi False)
c_1 = bool("0.0") # +
print(c_1)#True 

c_2 = bool("")
print(c_2)#False

# d.str -> int - działa zawsze (zaokrągla liczbę do całości w stronę zera)
d_1 = int(2.6) # +
print(d_1)#2

d_2 = int(-3.8)
print(d_2)#-3

# e.str -> float - działa zawsze kiedy podajemy cyfrę (zamienia tekst na ułamek)
e = float("2.5") # (Uwaga: możemy również podać liczbę całkowitą i będzie działać 😉)
print(e)#2.0

# f.bool -> float - działa zawsze (False zamienia na 0.0, a True zamienia na 1.0)
f = float(False) # +
print(f)#0.0

# g. bool -> int - działa zawsze (False zamienia na 0, a True zamienia na 1)
g = int(True) # +
print(g)#1

# h.int -> bool - działa zawsze (kiedy nic nie wpiszemy i kiedy wpiszemy 0 zamienia na False, a kiedy wpiszemy cokolwiek innego zamienia na True)
h = bool(0) # +
print(h)#False

# Dopisałem małą uwagę przy floatach. Zadanie samo w sobie bezbłędne. Brawo!

# 4.0 / 4.0