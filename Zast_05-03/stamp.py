from turtle import *

up()

goto(0, 0)
shape("arrow")
stamp()

goto(-100, -100)
shape("turtle")
stamp()

goto(-100, 100)
shape('square')
stamp()

goto(100, 100)
shape('triangle')
stamp()

goto(100, -100)
shape('classic')
stamp()

done()

# Proszę utworzyć następujące kształty:
# - kształt 'square' we współrzędnych X: -100, Y: 100
# - kształt 'triangle' we współrzędnych X: 100, Y: 100
# - kształt 'classic' we współrzędnych X: 100, Y: - 100