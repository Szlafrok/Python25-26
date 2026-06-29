lista = [[[[[[[[[[[[[[[[[123]]]]]]]]]]]]]]]]]

def wypisz(lista):
    zawartosc = lista[0]
    if isinstance(zawartosc, list):
        wypisz(zawartosc)
    else:
        print(zawartosc)

wypisz(lista)