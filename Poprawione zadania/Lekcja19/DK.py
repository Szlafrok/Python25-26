# Wrzucę sobie rozwiązania do funkcji żebym mógł je łatwiej sprawdzić

# QUIZ:
# 100 / 100

import random
# Z 2
def zad2():
    liczba = 1
    while liczba <= 100:
        if liczba / 3 == liczba // 3 and liczba / 5 == liczba // 5:
            print("FizzBuzz")
        elif liczba / 3 == liczba // 3:
            print("Fizz")
        elif liczba / 5 == liczba // 5:
            print("Buzz")
        else:
            print(liczba)
        liczba += 1
# Sprawdzanie podzielności jest bardzo niekonwencjonalne.
# Zwykle stosujemy n % x == 0. Ale bardzo sprytnie!
# 40 / 40

# Z 3
def wzorek(liczb):
    for i in range(1, liczb + 1):
        wiersz = (str(i) + " ") * i
        print(wiersz)
# Bardzo dobrze :)
# 40 / 40
        
# wzorek(7)

def najmnL(l):
    najm = l[0]
    for i in range(1, len(l)):
        if l[i] < najm:
            najm = l[i]
    return najm
print(najmnL([56, 32, 64 ,2 , 256]))

def najwl(l):
    najm = l[0]
    for i in range(1, len(l)):
        if l[i] > najm:
            najm = l[i]
    return najm
print(najwl([56, 32, 64 ,2, 128]))
# Bardzo dobrze :)
# 50 / 50

# # z 4 *
def trzynajml(l):
    a = l[0]
    b = l[1]
    c = l[2]

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a

    for i in range(3, len(l)):
        if l[i] < a:
            c = b
            b = a
            a = l[i]
        elif l[i] < b:
            c = b
            b = l[i]
        elif l[i] < c:
            c = l[i]

    return [a, b, c]
print(trzynajml([56, 32, 64 ,2 , 256]))

def trzynajw(l):
    a = l[0]
    b = l[1]
    c = l[2]

    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a

    for i in range(3, len(l)):
        if l[i] > a:
            c = b
            b = a
            a = l[i]
        elif l[i] > b:
            c = b
            b = l[i]
        elif l[i] > c:
            c = l[i]

    return [a, b, c]
print(trzynajw([56, 32, 64 ,2 , 256]))

# Bardzo dobrze!
# +10






# z 5
def ilew(c, s):
    return s.count(c)

print(ilew("b", "aa"))
# Trochę na skróty, ale jak najbardziej działa!

# 40 / 40



# z6
g, k = 0, 0
while True:
    w = input("orzel/reszka: ").lower()
    if w not in ["orzel","reszka"]: 
        pass
    r = random.choice(["orzel","reszka"])
    print(f"Wypadło: {r}")
    g, k = (g+1, k) if w==r else (g, k+1)
    print(f"Gracz: {g} | Komputer: {k}\n")
    if g>=10 and g-k>=2: 
        print("Wygrywasz!")
        break
    if k>=10 and k-g>=2: 
        print("Komputer wygrywa.")
        break

# Bardzo ładnie :)
# Jako ciekawostkę dodam, że można było zrobić warunek pętli z wartością bezwzględną:
# while (g < 10 and k < 10) or abs(g-k) < 2 

# 60 / 60 
# Bonus: + 10

"""
Podsumowanie:

Z1         100  /100
Z2          40  / 40
Z3          40  / 40
Z4          60  / 50
Z5          40  / 40
Z6          70  / 60
Z7          ---
=====================
Razem:     350 ⭐⭐⭐⭐⭐

Znakomicie!

"""