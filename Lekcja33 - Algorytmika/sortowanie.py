lista = [64, 34, 25, 12, 22, 11, 90]

# lista.sort()

print(lista)


def sortuj(lista): # sortowanie bąbelkowe
    n = len(lista)

    for i in range(n-1):
        for j in range(0, n-i-1):
            # zamienić elementy j i następny, jeśli j jest większy od następnego
            if lista[j] > lista[j+1]:
                # lista[j], lista[j+1] = lista[j+1], lista[j]
                pom = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = pom
    
    return lista

lista = sortuj(lista)
print(lista)