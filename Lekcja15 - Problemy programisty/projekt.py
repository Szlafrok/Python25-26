### Zadanie 1

def binarne_na_dzies(n: str) -> int: # z systemu binarnego
    res = 0 # result
    potega = 0
    for bit in reversed(n): # n[::-1]
        res += int(bit) * 2 ** potega
        potega += 1
    return res

print(binarne_na_dzies("100110110"))

# Zadanie 2

def dzies_na_binarne(n: int) -> str:
    wynik = ""
    while n > 0:
        wynik = str(n % 2) + wynik
        n //= 2
    return wynik

print(dzies_na_binarne(310))

# Palindrom to taki wyraz, który od tyłu czyta się tak samo, jak od przodu.
# Proszę napisać funkcję, która przyjmuje jako argument jakiś tekst (1 słowo)
# i zwraca True, jeśli to słowo jest palindromem, lub False, jeśli nie jest (+++)

# [Dod] Proszę przepisać tę funkcję tak, żeby ignorowała spacje i wielkość liter (+)

# Szablon funkcji:
def czy_palindom(t: str) -> bool:
    return t == t[::-1]

def czy_palindom(t: str) -> bool:
    i = 0
    j = len(t) - 1
    while i < j:
        if t[i] != t[j]: return False
        i += 1
        j -= 1
    return True

def czy_palindom(t: str) -> bool:
    odwrotny = ""
    for litera in t:
        odwrotny = litera + odwrotny

    return odwrotny == t


##### Pierwszość liczby


def czy_pierwsza(n: int) -> bool:
    if n < 2: return False
    d = 2
    while d < n:
        if n % d == 0:
            return False
        d += 1
    return True


from math import sqrt
def czy_pierwsza_faster(n: int) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    d = 3
    while d <= sqrt(n): # Gwiazdka dla osoby która wyjaśni dlaczego!
        if n % d == 0:
            return False
        d += 2
    return True