coords = [(0, 0), (-100, -100), (-100, 100), (100, 100), (100, -100)]
shapes = ["arrow", "turtle", "square", "triangle", "classic"]

from turtle import *

up()
for i in range(5):
    coordinate = coords[i]
    shape_ = shapes[i]
    goto(coordinate[0], coordinate[1])
    shape(shape_)
    stamp()
done()