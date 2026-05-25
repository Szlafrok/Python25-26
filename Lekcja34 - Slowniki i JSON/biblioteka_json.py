import json

with open("Lekcja34 - Slowniki i JSON/student.json", "r") as plik: # wczytanie z pliku
    student = json.load(plik)

print(student)

from pprint import pprint # pretty print
pprint(student)

print(student['kursy'])

student['kursy'].append('fizyka')

pprint(student)

# zapis do pliku
plik = open("Lekcja34 - Slowniki i JSON/student.json", "w")

json.dump(student, plik, indent = 4, sort_keys = True)