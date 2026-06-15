lista = [x for x in range(10, 2, -2)]
print(lista)

lista = [x+2 for x in range(1, 6)] # [ZMIENIAM coś na podstawie CZEGOŚ z danego PRZEDZIAŁU]
print(lista)

lista = [x**2 for x in range(1, 6)]
print(lista)

# Proszę utworzyć wyrażenie listowe, które utworzy listę złożoną ze
# wszystkich liczb PARZYSTYCH od 1 do 50. (++)

# [*] (+) Proszę zapisać liczby w liście w kolejności malejącej

lista = [x*2 for x in range(1, 26)]
lista = [x for x in range(50, 1, -2)]

lista = [x for x in range(1, 51) if x % 2 == 0]
               # 1. Wyciągam
                                 # 2. Sprawdzam
        # 3. Zamieszczam


print(lista) 


slowa = ["kebab", "ta", "awupa", "piłkarzyki", "nic", "płakał", "herobrine"]

print([slowo for slowo in slowa])

print(["aaa" + slowo for slowo in slowa])

print([slowo for slowo in slowa if len(slowo) > 5])

print(["aaa" + slowo for slowo in slowa if len(slowo) > 5])