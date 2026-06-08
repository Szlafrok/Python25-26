# zbiór - set

zbior = {1, 10, 2, 3, 4, 5, 6}

pusty = set()

zbior.add(9)
print(zbior)

zbior.add(4)
print(zbior)

zbior.remove(3)
print(zbior)

pusty.add(5)
print(zbior) # pułapka

zbior.discard(5)
#zbior.discard(1)

print(zbior)

wybrany = zbior.pop()
print(wybrany)
print(zbior)

zbior.clear()
print(zbior)

