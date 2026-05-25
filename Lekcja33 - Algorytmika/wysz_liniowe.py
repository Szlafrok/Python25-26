# Proszę zaimplementować algorytm wyszukiwania liniowego zgodnie z poniższym
# szablonem. 

# [3, 8, 10, 8, -3, -2]
#  0  1   2  3   4   5      dł 6

# range(6) -> 0, 1, 2, 3, 4, 5

def wysz_liniowe(T: list, szukana: int):
    n = len(T)
    for i in range(n):
        if T[i] == szukana:
            return i
    return None

lista = [3, 8, 10, 8, -3, -2]
print(wysz_liniowe(lista, 3)) # -> 0
print(wysz_liniowe(lista, 8)) # -> 1
print(wysz_liniowe(lista, -3)) # -> 4
print(wysz_liniowe(lista, 5)) # -> None