lista = [5, 4, 6, 2, 6, 1, 5, 2, 7, 11, 3]  # lista liczb, w której szukamy minimum i maksimum

def find_min(lista):
    lowest = lista[0]           # zakładamy, że najmniejszy jest pierwszy element
    for elem in lista:          # przechodzimy po wszystkich elementach
        if elem < lowest:       # jeśli znajdziemy mniejszy
            lowest = elem       # aktualizujemy minimum
    return lowest               # zwracamy najmniejszą wartość

def find_max(lista):
    highest = lista[0]          # zakładamy, że największy jest pierwszy element
    for elem in lista:          # przechodzimy po wszystkich elementach
        if elem > highest:      # jeśli znajdziemy większy
            highest = elem      # aktualizujemy maksimum
    return highest              # zwracamy największą wartość

print(find_min(lista))          # wypisuje najmniejszą liczbę z listy
print(find_max(lista))          # wypisuje największą liczbę z listy
