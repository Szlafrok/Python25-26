zachowanie = input("podaj ocene z zachwoania: wz, bdb, dobre")

matma = int(input("podaj ocenę z matematyki: "))
polski = int(input("podaj ocenę z języka polskiego: "))
historia = int(input("podaj ocenę z historii: "))
wf = int(input("podaj ocene z wf"))

srednia =( matma + polski + historia + wf)/ 4

if srednia >= 4.75 and zachowanie in ["bdb", "wz"]:
    print("bardzo dobrze masz pasek na koniec roku")
else:
    print("Nie masz paska na koniec powodzenia w nastepnym roku")