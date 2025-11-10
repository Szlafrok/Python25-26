tekst = "Kebabopoduszka"
print(len(tekst))

# exit()

for litera in tekst: # Dla każdej LITERY z TEKSTU
    print(litera, end = "__")    # wykonaj COŚ


# ZADANIE SAMODZIELNE

# Proszę napisać program z pętlą for, który wypisze zawartość zmiennej tekst
# (możemy tam wstawić dowolny tekst) oddzielając każdą literę znakiem spacji
print()
for litera in tekst:
    print(litera, end = " ")

print()
for i in range(8):
    print(i, end = " ")

print()
print("------------------")
tekst = "Kobyła ma mały bok"
print(tekst[0]) # -> K
print(tekst[2]) # -> b
print(tekst[5]) # -> o
#print(tekst[14]) # -> BŁĄD

for i in range(len(tekst)): # 
    print(tekst[i], end = " ")

print()
print("Odwrócony tekst:")
for i in range(len(tekst) - 1, -1, -1):
    print(tekst[i], end = " ")

# Proszę napisać wywołania range, które dadzą nam takie przedziały:

# 3 4 5 6 7
range(3, 8)

# 0 1 2 3 4 5 6 7 8

# 5 10 15 20

# 0 2 4 6 8 10

# -3 -2

# 9 5 1 -3