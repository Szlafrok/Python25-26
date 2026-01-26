def trojkat(a: int, b: int = 3, c: int = 4):
    print(a, b, c)
    if a >= b and a >= c:
        if b + c > a:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")
    elif b >= a and b >= c:
        if a + c > b:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")
    else: # c jest największe
        if a + b > c:
            print("Trójkąt istnieje")
        else:
            print("Trójkąt nie istnieje")

trojkat(2, 3, 10)

trojkat(2, 3) # istnieje: 2, 3, 4

trojkat(1, 1) # nie istnieje: 1, 1, 4

trojkat(b = 6, a = 8, c = 10)

#trojkat(4, a = 8, c = 10) błąd: podajemy 2 różne wartości a

trojkat(6, c = 10, b = 8)


# ZADANIE SAMODZIELNE!

# Proszę napisać funkcję, która przyjmuje jako argumenty stringa s oraz 
# liczbę x, a następnie wypisuje:

# - TAK, jeśli długość stringa s jest podzielna przez x
# - NIE, jeśli tak nie jest



# len(treść) - podaje liczbę znaków w danym stringu albo liczbę elementów listy
# % - reszta z dzielenia
# reszta z dzielenia jest równa 0 <=> liczby są podzielne

def podzielne(s: str, x: int) -> None:
    if len(s) % x == 0:
        print("TAK")
    else:
        print("NIE")

def power(podstawa: int, wykladnik: int) -> int:
    return podstawa ** wykladnik

print(power(2, 3) + 2)

def podzielne2(s: str, x: int) -> bool:
    if len(s) % x == 0:
        return True
    else:
        return False
    
print(podzielne2("kebabownia", 2))
print(podzielne2("kebabowniaa", 2))

def podzielne3(s, x):
    if len(s) % x == 0:
        return True
    return False

print(podzielne3("kebabownia", 2))
print(podzielne3("kebabowniaa", 2))

def podzielne4(s, x):
    return len(s) % x == 0

# Zadanko przykładowe

# Napisz funkcję, która jako argument otrzymuje listę elementów, w której mogą
# występować powtórzenia, a zwraca listę unikalnych elementów.
#Dla [1,2,3,3,3,3,4,5] oczekujemy [1, 2, 3, 4, 5]

# Należy zaprezentować instrukcję in: elem in lista

def powtorzenia(lista: list) -> list:
    unikaty = []
    for elem in lista:
        if elem not in unikaty:
            unikaty.append(elem)
    return unikaty

print(powtorzenia([1,2,3,3,3,3,4,5]))

import pygame