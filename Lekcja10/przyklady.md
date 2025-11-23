# PRZYKŁAD 1
Proszę napisać funkcję, która oceni, czy dana liczba naturalna jest parzysta
```py
def parzysta(n):
    if n % 2 == 0:
        print("Parzysta")
    else:
        print("Nieparzysta")
```

# PRZYKŁAD 2
Proszę napisać funkcję, która obliczy pole trapezu o podstawach a i b oraz wysokości h
```py
def pole(a, b, h):
    print((a + b) * h / 2)
```

# PRZYKŁAD 3
Proszę napisać funkcję, która obliczy średnią arytmetyczną liczb zawartych w liście. Lista zawiera wyłącznie liczby dziesiętne i całkowite.
```py
def srednia(liczby):
    print(sum(liczby) / len(liczby))
```