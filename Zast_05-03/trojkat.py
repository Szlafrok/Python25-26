# Proszę narysować trójkąt. Trójkąt powinien mieć 3 boki o długości
# równej 100.

from turtle import *
# t = turtle.Turtle()

width(5)
color("dark olive green")
fillcolor("yellow green")

begin_fill()
for i in range(3):
    forward(100)
    right(120)
end_fill()

done()

# Proszę narysować trójkąt o większych wymiarach i tak,
# aby był obrócony o 45 stopni.