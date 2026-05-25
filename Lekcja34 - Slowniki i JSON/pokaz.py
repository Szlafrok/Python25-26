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


