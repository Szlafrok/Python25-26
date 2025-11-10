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
tekst = "Kebabopoduszka"
print(tekst[0]) # -> K
print(tekst[2]) # -> b
print(tekst[5]) # -> o
#print(tekst[14]) # -> BŁĄD

for i in range(len(tekst)): # 
    print(tekst[i], end = " ")