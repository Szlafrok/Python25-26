student = {
    "imie": "Piotr",
    "wiek": 21,
    "wzrost": 185,
    "kursy": ["informatyka", "matematyka", "algorytmika"]
}

print(student["imie"])
# print(student["encepence"])

# .get()
print(student.get("imie"))
print(student.get("encepence")) # None

print(student.keys())

print(
    list(student.keys())
)

print(student.values())

print(
    list(student.values())
)

for key in student.keys():
    print(f"Hej, jestem kluczem - {key}")

for value in student.values():
    print(f"Hej, jestem wartością - {value}")


for pair in student.items():
    print(pair, pair[0], pair[1])

krotka = ("kremówka", "wuzetka")
ciasto2, ciasto1 = krotka # 2 elementy pozyskuję z 2-elementowego obiektu

print(ciasto1)
print(ciasto2)

for key, value in student.items():
    print(f"{key} - {value}")


##########################
def dictprint(slownik):
    print("{ -----")
    for key, value in slownik.items():
        print(f"{key}: {value}")
    print("----- }")


print("-----------------")

student.setdefault("ulubiona_gra", "Minecraft")
dictprint(student)

# pop - usuwa parę pod danym kluczem
deleted = student.pop("wzrost")
dictprint(student)
print(deleted)

# popitem - usuwa i zwraca ostatnią parę klucz-wartość
last_item = student.popitem()
dictprint(student)
print(last_item)

# przypisanie
student["hobby"] = "RPGi"
dictprint(student)

# usunięcie
del student["wiek"]
dictprint(student)

# update
student.update(
    {
        "nazwisko": "Polański",
        "lekcje": 2
    }
)
dictprint(student)

student.clear()
dictprint(student)