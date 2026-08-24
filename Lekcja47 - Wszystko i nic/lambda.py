# Proszę napisać funkcję, która przyjmuje argumenty a oraz b
# i zwraca wynik - ich sumę.

def suma(a, b): return a+b

print(suma(5, 6))


altersuma = lambda x, y: x + y
print(altersuma(5, 6))

# -----------------------

lista = [1, 5, 8, 21, 50, 40, 71]

lista.sort(key = lambda x: x % 10)
print(lista)