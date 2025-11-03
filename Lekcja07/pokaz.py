# Przypomnienie
zmienna = 5
if zmienna == 5:
    print("zmienna wynosi 5")
else:
    print("Zmienna nie wynosi 5")

d = 0

while d <= 4:
    print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
    d += 1

# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")
# print("Kaczka zabiła kaczkę kebabem a jajko pacmana")

import time

sekundy = int(input("Podaj liczbę sekund: "))

while sekundy > 0:
    print(f"{sekundy}...")
    time.sleep(1)
    sekundy -= 1
print("KABOOM!")