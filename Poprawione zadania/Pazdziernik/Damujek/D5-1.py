wojewodztwo = input()
pomniejszone = wojewodztwo.lower()


if pomniejszone == "śląskie" or pomniejszone == "podkarpackie" or pomniejszone == "lubelskie" or pomniejszone == "wielkopolskie" or pomniejszone == " lubuskie":
    print("Masz Ferie: 16 lutego – 1 marca 2026")
elif pomniejszone == "mazowieckie" or pomniejszone == "pomorskie" or pomniejszone == "podlaskie" or pomniejszone == "świętokrzyskie" or pomniejszone == "warmińsko-mazurskie" :
    print("Masz Ferie: 19 stycznia – 1 lutego 2026")
else:
    print("2 lutego – 15 lutego 2026")

# (+2 / 4)