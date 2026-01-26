# Proszę napisać program, który:

# - wczyta ocenę z zachowania
# - wczyta oceny z: matmy, polskiego, historii, wf

# i określi, czy otrzymamy pasek na świadectwie. Warunki paska:
# - średnia co najmniej 4.75 (suma ocen / liczba ocen)
# - zachowanie co najmniej bardzo dobre (5)

zachowanie = int(input("Podaj ocenę z zachowania"))
matma = int(input("Podaj ocenę z matmy"))
polski = int(input("Podaj ocenę z polskiego"))
historia = int(input("Podaj ocenę z historii"))
wf = int(input("Podaj ocenę z wf-u"))

srednia = (matma + polski + historia + wf) / 4

if srednia >= 4.75 and zachowanie >= 5:
    print("Masz pasek!")
else:
    print("Nie masz paska!")