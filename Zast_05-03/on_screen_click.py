from turtle import *

up()

def after_click(x, y):
    print('test')
    goto(x, y)
    down()
    dot(15)
    up()

onscreenclick(after_click)

#after_click(0, 0)

done()